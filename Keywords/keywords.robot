*** Settings ***
Library  SeleniumLibrary
Library    String
Library    DateTime
Resource    ../Locators/locators.robot
Resource    ../Locators/user_inputs.robot
             									

*** Keywords ***
HQ Login
    Open Browser    ${LOGIN URL}    ${BROWSER}
    Set Selenium Implicit Wait  ${implcit_wait_time}
    Maximize Browser Window
    Input Text    ${username}    ${email}
    Input Text    ${password}   ${pass}
    ${IsElementVisible}=  Run Keyword And Return Status    Element Should Be Visible   ${confirm_cookie}
    Run Keyword If     ${IsElementVisible}    Click Element  ${confirm_cookie}
    Click Button  ${submit_button}
    Title Should Be    ${commcare hq title} 
    #Run Keyword And Ignore Error     Click Element    ${confirm_cookie}
    Open Web App
    

Open Web App
   Click Element    ${webapps_menu}
   
Log in as ct_user
   Sync App
   Click Element    ${login_as}
   Click Element    ${ct_user}
   Sleep    2s
   Click Element    ${confirm_user_login}
   Sync App
   Click Element    ${select_app} 
   

Register contact with phone number
   Wait Until Element Is Enabled    ${register_new_contacts_menu}
   Sleep    1s    
   Click Element    ${register_new_contacts_menu}
   Click Element    ${select_first case_in_caselist}
   Click Element    ${continue}
   Click Element    ${register_new_contacts_form} 
   ${hex} =    Generate Random String	4	[NUMBERS]abcdef
   ${first_name_random} =     Catenate	SEPARATOR=-	User	${hex}
   Set Suite Variable  ${first_name_random} 
   Input Text       ${contact_first_name}    ${first_name_random}
   ${mobile_number}=    Generate random string        10     0123456789
   Input Text       ${contact_phone_num}    ${mobile_number}
   Execute JavaScript    document.evaluate("${preferred_language}",document.body,null,9,null).singleNodeValue.click();
   Execute JavaScript    document.evaluate("${first_symptom_date}",document.body,null,9,null).singleNodeValue.click();
   ${yesterday's_date} =    Get Current Date    result_format=%m/%d/%Y    increment=-1 day
   Input Text    ${first_symptom_date}    ${yesterday's_date}
   Execute JavaScript    document.evaluate("${first_symptom_date}",document.body,null,9,null).singleNodeValue.click();
   Execute Javascript    document.evaluate(" ${submit_form}",document.body,null,9,null).singleNodeValue.click();
   Element Should Be Visible    ${success_message}    
   
Open App Home Screen
    Sleep    3s
    Wait Until Element Is Visible    ${app_home}  
    Wait Until Element Is Enabled    ${app_home}     
    Click Element    ${app_home}
      
Open WebApp Home
    Sleep    3s
    Wait Until Element Is Enabled    ${webapps_home}
    Click Element    ${webapps_home}

Open All Contacts Unassigned & Open menu 
        Sleep    2s
        Open App Home Screen
        Wait Until Element Is Visible     ${contacts_unassigned_open_menu}
        Wait Until Element Is Enabled      ${contacts_unassigned_open_menu}
        Sleep    2s
        Execute JavaScript    document.evaluate("${contacts_unassigned_open_menu}",document.body,null,9,null).singleNodeValue.click();


Search in the case list    
        ${first_name_random}   Get Variable Value    ${first_name_random}   
        Log    ${first_name_random}
        Input Text    ${search_case}    ${first_name_random}
        Click Element    ${search_button} 
       
 
Convert contact to PUI using CM form
        Open All Contacts Unassigned & Open menu
        Search in the case list
        Select Created Case    
        Click Element    ${contact_monitoring_form}
        Wait Until Element Is Enabled    ${initial_interview_disposition}    
        Execute JavaScript    document.evaluate("${initial_interview_disposition}",document.body,null,9,null).singleNodeValue.click();
        Execute JavaScript    document.evaluate("${race}",document.body,null,9,null).singleNodeValue.click();
        Execute JavaScript    document.evaluate("${ethnicity}",document.body,null,9,null).singleNodeValue.click();
        Execute JavaScript    document.evaluate("${gender}",document.body,null,9,null).singleNodeValue.click();
        Execute JavaScript    document.evaluate("${symptom_congestion}",document.body,null,9,null).singleNodeValue.click();
        Execute JavaScript    document.evaluate("${symptom_fatigue}",document.body,null,9,null).singleNodeValue.click();
        Execute JavaScript    document.evaluate("${symptom_fever}",document.body,null,9,null).singleNodeValue.click();
        Execute JavaScript    document.evaluate("${symptom_runny_nose}",document.body,null,9,null).singleNodeValue.click();
        Wait Until Element Is Enabled    ${date_of_symptomp_onset} 
        Execute JavaScript    document.evaluate("${date_of_symptomp_onset}",document.body,null,9,null).singleNodeValue.click();
        ${yesterday's_date} =    Get Current Date    result_format=%m/%d/%Y    increment=-1 day
        Input Text    ${date_of_symptomp_onset}    ${yesterday's_date}
        Execute JavaScript    document.evaluate("${date_of_symptomp_onset}",document.body,null,9,null).singleNodeValue.click();
        Execute JavaScript    document.evaluate("${yes_convert_pui}",document.body,null,9,null).singleNodeValue.click();
        Wait Until Element Is Enabled     ${submit_form}
        Execute JavaScript    document.evaluate("${submit_form}",document.body,null,9,null).singleNodeValue.click()
     
   
PUI form submission
    Wait Until Element Is Enabled    ${confirm_yes_convert_pui}
    Execute JavaScript    document.evaluate("${confirm_yes_convert_pui}",document.body,null,9,null).singleNodeValue.click();
    Wait Until Element Is Enabled    ${submit_form} 
    Execute JavaScript    document.evaluate("${submit_form}",document.body,null,9,null).singleNodeValue.click()
    
Convert contact to PUI form
    Open All Contacts Unassigned & Open menu
    Search in the case list
    Select Created Case
    Wait Until Element Is Enabled    ${covert_to_pui_form}
    Execute JavaScript    document.evaluate("${covert_to_pui_form}",document.body,null,9,null).singleNodeValue.click() 
    PUI form submission
      
Select Created Case
    ${first_name_random}   Get Variable Value    ${first_name_random}  
    ${contact_created}   Set Variable    //td[text()='${first_name_random}' and @class='module-caselist-column']
    Set Suite Variable    ${contact_created}     
    Wait Until Element Is Enabled    ${contact_created} 
    Sleep    2s      
    Execute JavaScript    document.evaluate("${contact_created}",document.body,null,9,null).singleNodeValue.click()     
    Wait Until Element Is Enabled    ${continue}
    Sleep    2s 
    Scroll Element Into View    ${continue}
    Click Element    ${continue}    
    
Log in as ci_user
   Sync App
   Click Element    ${login_as}
   Click Element    ${ci_user}
   Sleep    2s
   Click Element    ${confirm_user_login}
   Sleep    2s
   Sync App
   Click Element    ${select_app} 
    
All Suspected Cases (PUIs) menu
    Sleep    2s
    Wait Until Element Is Enabled    ${all_suspected_cases_menu} 
    Click Element    ${all_suspected_cases_menu} 

Search Archieved Case in All Suspected Cases (PUIs) menu
    All Suspected Cases (PUIs) menu
    Wait Until Element Is Enabled    ${search all cases}
    Execute JavaScript    document.evaluate(" ${search all cases}",document.body,null,9,null).singleNodeValue.click() 
    Input Text    ${first-name_case_search}    ${archieved_contact_name}
    Wait Until Element Is Enabled    ${case search submit}
    Execute JavaScript    document.evaluate("${case search submit}",document.body,null,9,null).singleNodeValue.click()

Search Case in All Suspected Cases (PUIs) menu
    All Suspected Cases (PUIs) menu
    Wait Until Element Is Enabled    ${search all cases}
    Execute JavaScript    document.evaluate(" ${search all cases}",document.body,null,9,null).singleNodeValue.click() 
    Wait Until Element Is Enabled    ${case search submit}
    Execute JavaScript    document.evaluate("${case search submit}",document.body,null,9,null).singleNodeValue.click() 
    
    
Change PUI Status form
    Wait Until Element Is Enabled    ${change pui status form}
    Execute JavaScript    document.evaluate("${change pui status form}",document.body,null,9,null).singleNodeValue.click()
    Wait Until Element Is Enabled    ${convert_back_to_contact}
    Execute JavaScript    document.evaluate(" ${convert_back_to_contact}",document.body,null,9,null).singleNodeValue.click()  

    
Yes, Close the Record
    Wait Until Element Is Enabled    ${are_you_sure}
    Execute JavaScript    document.evaluate(" ${are_you_sure}",document.body,null,9,null).singleNodeValue.click()  
    Wait Until Element Is Enabled     ${close_record}
    Click Element    ${close_record}
    Element Should Be Visible    ${close_yes_message}  
    Element Should Be Visible    ${close_yes_message2} 
    Wait Until Element Is Enabled    ${final_disposition}
    Execute JavaScript    document.evaluate("${final_disposition}",document.body,null,9,null).singleNodeValue.click()
    
    #Would you like to send the quarantine release notice by email?  no 
    Wait Until Element Is Enabled    ${like to send mail no}
    Execute JavaScript    document.evaluate("${like to send mail no}",document.body,null,9,null).singleNodeValue.click() 
    Element Should Be Visible       ${ send the release from quarantine notice by mail question} 
    #Do you want to send the release from quarantine notice by mail?  yes
    Wait Until Element Is Enabled  ${send quarantine mail yes}
    Execute JavaScript    document.evaluate("${send quarantine mail yes}",document.body,null,9,null).singleNodeValue.click() 
    Element Should Be Visible     ${date_notice_sent} 
    #Do you want to send the release from quarantine notice by mail?  no
    Wait Until Element Is Enabled    ${send quarantine mail no}
    Execute JavaScript    document.evaluate("${send quarantine mail no}",document.body,null,9,null).singleNodeValue.click()
    Wait Until Page Does Not Contain    ${date_notice_sent}    
    Element Should Not Be Visible     ${date_notice_sent}     
    Element Should Be Visible    ${no notice label}
    
    ###Would you like to send the quarantine release notice by email? yes   
    Wait Until Element Is Enabled    ${like to send mail yes}
    Execute JavaScript    document.evaluate("${like to send mail yes}",document.body,null,9,null).singleNodeValue.click()  
    Input Text    ${what_address}    ${email_input}
    ## toprocess the input
    Execute JavaScript    document.evaluate("${like to send mail yes}",document.body,null,9,null).singleNodeValue.click() 
    Element Should Be Visible    ${mail_label} 
    #label to process
    Execute JavaScript    document.evaluate("${like to send mail yes}",document.body,null,9,null).singleNodeValue.click()
    Wait Until Element Is Enabled     ${submit_form}
    Execute JavaScript    document.evaluate("${submit_form}",document.body,null,9,null).singleNodeValue.click() 
    
No , Close the Record
    Wait Until Element Is Enabled    ${are_you_sure}
    Execute JavaScript    document.evaluate(" ${are_you_sure}",document.body,null,9,null).singleNodeValue.click()  
    Wait Until Element Is Enabled     ${dont_close_record} 
    Click Element    ${dont_close_record} 
    Element Should Be Visible    ${close_no_message}
    Element Should Be Visible    ${close_no_message2}
    Wait Until Element Is Enabled     ${submit_form}
    Execute JavaScript    document.evaluate("${submit_form}",document.body,null,9,null).singleNodeValue.click() 
 
    
All Closed Contacts menu
    Wait Until Element Is Enabled    ${all_closed_contacts_menu}
    Click Element    ${all_closed_contacts_menu}
     
All Open Contacts menu
    Open App Home Screen
    Reload Page
    Wait Until Element Is Enabled    ${all_open_contacts_menu} 
    Click Element    ${all_open_contacts_menu} 
        
Search and Select Archieved Case
    Search Archieved Case
    When Wait Until Element Is Enabled    ${archieved_contact}   
    Sleep    2s 
    Click Element    ${archieved_contact} 
    Click Element    ${continue}
    
Yes, Close the Archieved Record
    Wait Until Element Is Enabled     ${close_record}
    Click Element    ${close_record}
    Element Should Be Visible    ${no_longer_active_message}  
    Wait Until Element Is Enabled    ${final_disposition2} 
    Click Element     ${final_disposition2}    
    Wait Until Element Is Enabled     ${submit_form}
    Execute JavaScript    document.evaluate("${submit_form}",document.body,null,9,null).singleNodeValue.click() 
    
No , Close the Archieved Record
    Wait Until Element Is Enabled     ${dont_close_record} 
    Click Element    ${dont_close_record} 
    Element Should Be Visible    ${no_longer_active_message}  
    Wait Until Element Is Enabled     ${submit_form}
    Execute JavaScript    document.evaluate("${submit_form}",document.body,null,9,null).singleNodeValue.click() 
     
Search Archieved Case
    Input Text    ${search_case}    ${archieved_contact_name}
    Click Element    ${search_button}
    
Sync App
    Open WebApp Home
    Click Element    ${sync}
    Sleep    5s
    Wait Until Element Is Visible    ${sync success}    
 
    
