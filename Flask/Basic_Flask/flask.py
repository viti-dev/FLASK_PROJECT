from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST']) # To render Homepage
def home_page():
    # return "render_template('index.html')"
    return render_template('index.html')

@app.route('/math', methods=['POST'])  # This will be called from UI
def math_operation():
    if (request.method=='POST'):
        operation=request.form['operation']
        print('==================\n\n\n=======', operation)
        num1=int(request.form['num1'])
        num2 = int(request.form['num2'])
        print('=============', num1, num2)
        if(operation=='add'):
            r=num1+num2
            result= 'the sum of '+str(num1)+' and '+str(num2) +' is '+str(r)
        if (operation == 'subtract'):
            r = num1 - num2
            result = 'the difference of ' + str(num1) + ' and ' + str(num2) + ' is ' + str(r)
        if (operation == 'multiply'):
            r = num1 * num2
            result = 'the product of ' + str(num1) + ' and ' + str(num2) + ' is ' + str(r)
        if (operation == 'divide'):
            r = num1 / num2
            result = 'the quotient when ' + str(num1) + ' is divided by ' + str(num2) + ' is ' + str(r)
            print('============', result)
        return render_template('results.html',result=result)

@app.route('/via_postman', methods=['POST']) # for calling the API from Postman/SOAPUI
def math_operation_via_postman():
    if (request.method=='POST'):
        operation=request.json['operation']
        num1=int(request.json['num1'])
        num2 = int(request.json['num2'])
        if(operation=='add'):
            r=num1+num2
            result= 'the sum of '+str(num1)+' and '+str(num2) +' is '+str(r)
        if (operation == 'subtract'):
            r = num1 - num2
            result = 'the difference of ' + str(num1) + ' and ' + str(num2) + ' is ' + str(r)
        if (operation == 'multiply'):
            r = num1 * num2
            result = 'the product of ' + str(num1) + ' and ' + str(num2) + ' is ' + str(r)
        if (operation == 'divide'):
            r = num1 / num2
            result = 'the quotient when ' + str(num1) + ' is divided by ' + str(num2) + ' is ' + str(r)
        return jsonify(result)


if __name__ == '__main__':
    app.run(debug=True)
    # app.run(host="0.0.0.0", port=5000)





















# context = "{'form_view_ref':'oss_contact.view_res_organisation_contact_form'}"
# >:- for default view for any m2m or o2m field
# priority (for set view seq)
# offset for default search record(ex 10 to 50)
# dpkg -L (press tab for all pkg)  :- for pkg location search
# dpkg -L google-chrome-stable
# dpkg -L Chrome\chromedriver.exe







# CMD for Ubuntu
# ls -l   :- -l to see details like file size, permission, modified
# cat filename  :- read text file
# touch new_file_name :- create new files
# mkdir new_dir  :- create folders
# cp existing_file.txt existing_file.back   :- copy files or folders
# mv file.txt new_file.txt   :- rename file name
# rm filename  :- remove file
# nano filename   :- edit file
#  clear  :- clear terminal screen
#  ps aux :- running process
# top :- system monitor
#  lsblk  :- list disk and partitions
# sudo fdisk -l   :-  List and manage disks and partitions
# find . -type f -name "*.txt"   :- search file
# ps aux | grep -i “name of your desired program”
# chmod u+x file executable   (chmod -r 777):- for access permission
# lshw  :- hardware details
# lshw -C network

# apt: Install, remove and manage .deb packages
# sudo apt install package_name
# sudo apt remove package_name
# sudo apt update && sudo apt upgrade
# ip a    :- check ip address
# man command_name  (man ls):- for learn cmd




# sudo apt-get update
# sudo apt-get --only-upgrade install google-chrome-stable



'204 o m s ai'