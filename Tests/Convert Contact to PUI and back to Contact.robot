*** Settings ***
Documentation     This is a POC for USH AppsTesting the workflow to convert a symptomatic contact into a suspected case (PUI) and testing the workflow to convert a suspected case (PUI) back into a contact.
Library  SeleniumLibrary
Resource    ../Keywords/keywords.robot
Suite Setup    HQ Login
  
       
*** Test Cases ***

Convert_Contact_to_PUI_1
    [Documentation]    Convert contact to PUI using "Contact Monitoring" form					
    Log in as ct_user
    Register contact with phone number
    Convert contact to PUI using CM form
    Page Should Contain Element    ${pui_form_header} 
    PUI form submission
    Open All Contacts Unassigned & Open menu
    Search in the case list
    ${contact_created}   Get Variable Value    ${contact_created}
    Element Should Not Be Visible    ${contact_created}   
    
Convert_Contact_to_PUI_3
    [Documentation]    Convert PUI back to contact - close record   
    Log in as ci_user	
    Search Case in All Suspected Cases (PUIs) menu
    Search in the case list 
    Select Created Case
    Change PUI Status form
    Yes, Close the Record 
    ## Redirects to All Suspected Cases (PUIs) menu
    Search in the case list
    ${contact_created}   Get Variable Value    ${contact_created}
    Element Should Not Be Visible    ${contact_created}   
    Log in as ct_user
    All Closed Contacts menu
    Search in the case list
    Element Should Be Visible    ${contact_created}    
    All Open Contacts menu
    Search in the case list
    Element Should Not Be Visible    ${contact_created}    
    
Convert_Contact_to_PUI_2	
    [Documentation]    Convert contact to PUI using "Convert Contact to Suspected Case (PUI)" form
    Open App Home Screen
    Register contact with phone number
    Convert contact to PUI form
    Open All Contacts Unassigned & Open menu
    Search in the case list
    ${contact_created}   Get Variable Value    ${contact_created}
    Element Should Not Be Visible    ${contact_created}    Contact appearing in menu
    
Convert_Contact_to_PUI_4
    [Documentation]    Convert PUI back to contact - do not close record
    Log    Sleeping ES to update..
    Sleep     2 minutes	
    Log in as ci_user	 
    Search Case in All Suspected Cases (PUIs) menu
    Search in the case list
    Select Created Case
    Change PUI Status form	
    No , Close the Record
    ## Redirects to All Suspected Cases (PUIs) menu
    Search in the case list
    ${contact_created}   Get Variable Value    ${contact_created}
    Element Should Not Be Visible    ${contact_created}   
    Log in as ct_user 
    All Open Contacts menu
    Search in the case list
    Element Should Be Visible    ${contact_created}   
    
Convert_Contact_to_PUI_6
    [Documentation]    convert PUI back to contact (archived contact) - do not close record					
    Log in as ci_user	
    Search Archieved Case in All Suspected Cases (PUIs) menu
    Search and Select Archieved Case
    Change PUI Status form
    No , Close the Archieved Record
    Search Archieved Case 
    Element Should Be Visible    ${archieved_contact}   
    
Convert_Contact_to_PUI_5
    [Documentation]    convert PUI back to contact (archived contact) - close record					
    Log in as ci_user	
    Search Archieved Case in All Suspected Cases (PUIs) menu
    Search and Select Archieved Case
    Change PUI Status form
    Yes, Close the Archieved Record
    Search Archieved Case 
    Element Should Not Be Visible     ${archieved_contact} 
        