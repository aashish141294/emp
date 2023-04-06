from abc import ABC,abstractmethod

'''BaseCtl is inherited by all application cotroller'''

class BaseCtl(ABC):
    # contains preload data
    preload_data = {}

    # contains list of objeccts ,it will displayed at page
    page_list = {}

    '''
    initialize contriller attributes
    '''

    def __init__(self):
        self.form = {}
        self.form["pageNo"] = 1
        self.form["id"] = 0
        self.form["message"] =""
        self.form["error"] = False
        self.form["inputError"] = {}
        self.form["data"] = {}
        self.form["sessionkey"] = ""

    '''
    It loads prelod data of the page
    '''
    def preload(self,request):
        print("This is Preload")

    '''
    Display record of recieved ID
    '''
    def display(self,request,params={}):
        pass

    '''
    Submit data
    '''
    def submit(self,request,params={}):
        pass

    '''
    Populate values from request POST/GET to controller form object
    '''
    def request_to_form(self,requestForm):
        pass

    # Populate Form from Model
    def model_to_form(self,obj):
        pass

    # Convert form into Module
    def form_to_model(self,obj):
        pass

    '''
    Apply input validation
    '''

    def input_validation(self):
        self.form['error'] = False
        self.form['message'] = ''

    # To get previous records
    def previous(self,request,params={}):
        pass

    # To get next records
    def next(self,request,params={}):
        pass

    '''
    Returns template of controller
    '''
    def get_template(self):
        pass

    def get_service(self):
        pass
