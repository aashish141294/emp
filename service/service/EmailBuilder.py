from Area52.settings import EMAIL_HOST_USER,BASE_DIR
from string import Template


class EmailBuilder:
    template_dir = BASE_DIR +"/" + "service/template/"
    @staticmethod
    def sign_up(params):
        msg =""
        msg+="<HTML><BODY>"
        msg+="registration is Successful for ors project"
        msg+= "<p><b>Login Id : "+params["Email"] +"<br>" + " Password: "+params["Password"]+"</b></p>"
        msg+="</BODY></HTML>"
        return msg

    
    @staticmethod
    def change_password(params):
        msg=""
        msg+="<HTML><BODY>"
        msg+= "<h2>"+"Your password has been change successfully !!"+params.FirstName+"" +params.LastName+"</h2>"
        msg+="<p><b>"+"To access your account user login id:" +params.Email+ "<br>" +"Password :"+params.Password+"</b><p>"
        msg+="</HTML></BODY>"
        return msg
    
    
    @staticmethod
    def forget_password(params):
        print("000000000009--",params)
        print("------------->",params.FirstName)
        msg=""
        msg+="<HTML><BODY>"
        msg+="<H1>"+"YOUR PASSWORD IS RECOVERED "+ params.FirstName+" "+ params.LastName + "</H1>"
        msg+="<P><B>"+"To access account user login id: "+params.Email+"<br>"+" Password: "+params.Password
        msg+="</HTML></BODY>"
        return msg
