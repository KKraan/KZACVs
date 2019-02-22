"""
Choice script for the robotframework tests.

This file should be placed in the telfortRobot main folder in order for it to run.
"""
import os
import sys
from datetime import datetime 


ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
os.chdir(ROOT_DIR)
timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
output = " --outputdir Build/Build" + timestamp

global browser
global metadata

metadata = {}

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


# Select the environment on which the tests should run
def select_environment():
    global environment

    menu_item = int(sys.argv[1]) if len(sys.argv) > 1 else 0
    environment_url = ''
    # add gateway id URL for token requests
    gateway_id_url = "https://mobieltest.telfort.nl/gw/uat/id"
    print("What environment do you want to run your tests on?")
    print("1. Production")
    print("2. DevB")
    print("3. DevD")
    print("4. DevE")
    print("5. DevF")
    print("6. TestA")
    print("7. TestB")
    print("8. TestC")
    print("9. TestD")
    print("10. AcceptA")
    print("11. AcceptB")
    print("12. AcceptC")
    print("13. AcceptD")
    print("14. Quit")
    if menu_item == 0:
        menu_item = int(input("Pick an item from the menu: "))
    if menu_item == 1:
        environment_url = "https://www.telfort.nl"
        gateway_id_url = "https://mobiel.telfort.nl/gw/id"
    elif menu_item == 2:
        environment_url = "https://devb.1mijn.telfort.nl"
        gateway_id_url = "https://mobieltest.telfort.nl/gw/team-blue/uat/id"
    elif menu_item == 3:
        environment_url = "https://devd.1mijn.telfort.nl"
        gateway_id_url = "https://mobieltest.telfort.nl/gw/team-red/uat/id"
    elif menu_item == 4:
        environment_url = "https://deve.1mijn.telfort.nl"
    elif menu_item == 5:
        environment_url = "https://devf.1mijn.telfort.nl"
    elif menu_item == 6:
        environment_url = "https://testa.1mijn.telfort.nl"
    elif menu_item == 7:
        environment_url = "https://testb.1mijn.telfort.nl"
    elif menu_item == 8:
        environment_url = "https://testc.1mijn.telfort.nl"
    elif menu_item == 9:
        environment_url = "https://testd.1mijn.telfort.nl"
    elif menu_item == 10:
        environment_url = "https://accepta.1mijn.telfort.nl"
        # check accepta EP for token requests
        gateway_id_url = "https://mobielpreprod.telfort.nl/gw/id"
    elif menu_item == 11:
        environment_url = "https://acceptb.1mijn.telfort.nl"
        gateway_id_url = "https://mobielpreprod.telfort.nl/gw/id"
    elif menu_item == 12:
        environment_url = "https://acceptc.1mijn.telfort.nl"
    elif menu_item == 13:
        environment_url = "https://acceptd.1mijn.telfort.nl"
    elif menu_item == 14:
        clear()
        sys.exit("Closing down script")

    environment = " -v SERVER:" + environment_url + " -v GW_ID_URL:" + gateway_id_url

    global metadata
    metadata['Telfort Endpoint FE'] = environment_url
    metadata['Telfort Endpoint API'] = gateway_id_url

    clear()
    print("Selected environment: " + environment_url)
    print("")

# Select the testdata set that should be used for the testcases.
def select_testdata():
    global testdata
    global included_tags
    menu_item = int(sys.argv[2]) if len(sys.argv) > 2 else 0

    testdata_file = ''
    print("UAT or Production testdata?")
    print("1. Production testdata")
    print("2. UAT testdata")
    print("3. Quit")
    if menu_item == 0:
        menu_item = int(input("Pick an item from the menu: "))
    if menu_item == 1:
        testdata_file = "Production_Accounts.yaml"
        included_tags = " -i Prod"
    elif menu_item == 2:
        testdata_file = "UAT_Accounts.yaml"
        included_tags = " -i UAT"
    elif menu_item == 3:
        clear()
        sys.exit("Closing down script")

    testdata = " -V src/Configuration/" + testdata_file

    global metadata
    metadata['Telfort Dataset'] = testdata_file

    clear()
    print("Selected testdatafile: " + testdata_file)
    print("")

# Select the testcases that you want to run
def select_testcase():

    tests = [
        { 'name': 'Full Regression',                    'path': 'src/TestCases',                                                },
        { 'name': 'LPR',                                'path': 'src/TestCases',                            'tags': [ 'LPR' ]   },
        { 'name': 'Login Tests',                        'path': 'src/TestCases/Closed/LoginTests',                              },
        { 'name': 'Regression Mijn Telfort',            'path': 'src/TestCases/Closed',                                         },
        { 'name': 'Regression Business Environment',    'path': 'src/TestCases/Business',                                       },
        { 'name': 'Regression Open Environment',        'path': 'src/TestCases/Open',                                           },
        { 'name': 'Regression Reseller',                'path': 'src/TestCases/Closed/E2E/Reseller*',                           },
        { 'name': 'Regression Residential',             'path': 'src/TestCases/Closed/E2E/Residential*',                        },
        { 'name': 'LPR Mijn Telfort',                   'path': 'src/TestCases/Closed',                     'tags': [ 'LPR' ]   },
        { 'name': 'LPR Business Environment',           'path': 'src/TestCases/Business',                   'tags': [ 'LPR' ]   },
        { 'name': 'LPR Open Environment',               'path': 'src/TestCases/Open',                       'tags': [ 'LPR' ]   },
        { 'name': 'Test tags',                          'path': 'src/TestCases',                            'tags': [ 'Test' ]  },
    ]

    menu_item = int(sys.argv[3]) if len(sys.argv) > 3 else -1
    print("Which testcase do you want to run?")
    print("0. Quit")
    for num, test in enumerate(tests, start=1):
        print("{}. {}".format(num, test['name']))

    if menu_item == -1:
        menu_item = int(input("Pick an item from the menu: "))

    if menu_item == 12:
        included_tags = " "

    if menu_item == 0:
        clear()
        sys.exit("Closing down script")
    else:
        global testcase

        testcase = ""

        # Always include the prechecks.
        # testcase += " src/TestCases/00-PreTestChecks.robot"
        testcase += " " + tests[menu_item - 1]['path']

        # Add tags
        if 'tags' in tests[menu_item - 1]:

            for num, tag in enumerate(tests[menu_item - 1]['tags'], start=1):
                testcase = "-i " + tag + " " + testcase

            if 'LPR' in tests[menu_item - 1]['tags']:
                # If LPR is selected, any UAT/Prod tags should not be used.
                global included_tags
                included_tags = ''


    global metadata
    metadata['Telfort Testset'] = testcase

    clear()

def select_browser():

    browsers = [
        { 'name': 'Chrome',              'value': 'chrome' },
        { 'name': 'Chrome (headless)',   'value': 'headlesschrome' },
    ]

    menu_item = int(sys.argv[4]) if len(sys.argv) > 4 else -1
    print("Select browser to run tests with.")
    print("0. Quit")
    for num, b in enumerate(browsers, start=1):
        print("{}. {}".format(num, b['name']))

    if menu_item == -1:
        menu_item = int(input("Pick an item from the menu: "))

    if menu_item == 0:
        clear()
        sys.exit("Closing down script")

    global browser
    browser_value = browsers[menu_item - 1]['value']
    browser = "-v BROWSER:{}".format(browser_value)

    global metadata
    metadata['Telfort Browser'] = browser_value

    clear()

# Function to start the robot tests. This combines all the variables for the command line and opens the report.
def start_robot_tests():

    robot_command = "robot "

    global metadata
    for label in metadata:
        robot_command += "-M \"{}:{}\" ".format(label, metadata[label])

    robot_command += "{} {} {} {} {} {}".format(environment, browser, included_tags, testdata, output, testcase)
    print('Starting robot tests using command: ' + robot_command)
    os.system(robot_command)
    if os.name == 'nt':
        open_file(ROOT_DIR + '\\Build\\Build' + timestamp + '\\report.html')
    else:
        open_file('Build/Build' + timestamp + '/report.html')


# The actual order in which these functions are started
# These can be done in any order, except for the start Robot Tests function, which has to be done last.
clear()
select_environment()
select_testdata()
select_testcase()
select_browser()
start_robot_tests()
