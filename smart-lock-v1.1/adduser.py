import noor_headshots as hs
import train_model as tm
import fp_enroll as fp
import WWrite as rw
import userdb
import lcd_display
import del_user

def enroll_new_user(uname,empId):
#     lcd_display.display_msg('CREATING DATASET',' LOOK IN CAMERA ')
    if hs.headshots(uname):
#         lcd_display.display_msg('DATASET CREATED ','  SUCESSFULLY ')
#         lcd_display.display_msg('    TRAINING    ','   THE MODEL   ')
        if tm.trainmodel():
            if fp.enroll_finger(empId):
                rfidRegistered,rfid= rw.writeRFID(uname)
                if rfidRegistered == True:
                    #create a profile in userdb
                    print('user successfully registered')
                    userdb.enroll(uname,empId,rfid)
                else :
                    print('rfid error')
                    del_user.delete_dataset(uname,empId)
            else :
                del_user.delete_dataset(uname,empId)
                print('fp error')
        else :
            del_user.delete_dataset(uname,empId)
            print('train error')
    else :
        del_user.delete_dataset(uname,empId)  
        print('dataset error')