*** Settings ***
Resource    ../Locators/user_inputs.robot


*** Variables ***
${LOGIN URL}      https://www.commcarehq.org/accounts/login/
${BROWSER}        Chrome

${username}    id:id_auth-username
${password}    id:id_auth-password
${submit_button}    //button[@type="submit"]
${confirm_cookie}    css:#hs-eu-confirmation-button
${commcare hq title}    CommCare HQ
${webapps_menu}    css:#CloudcareTab > a
${login_as}    css:.js-restore-as-item
${ct_user}    css:[aria-label='auto_poc'] > .module-column-name
${ci_user}    css:[aria-label='ci_poc'] > .module-column-name
${confirm_user_login}    //button[@id="js-confirmation-confirm"]

${select_app}    xpath://div[@aria-label='NY-CDCMS: Web Apps Testing POC']
${register_new_contacts_menu}    xpath:(//div[@aria-label='Register New Contact(s)']/div)[1]
${select_first case_in_caselist}    xpath:(//td[@class='module-caselist-column'])[1]
${continue}    id:select-case
${register_new_contacts_form}    xpath://tr[@aria-label="Register New Contact(s)"]
${contact_first_name}     xpath://span[text()='First name']/following::div[1]/div[@class='widget']/descendant::textarea
${contact_phone_num}    xpath://span[text()='Phone number:']/following::div[1]/div[@class='widget']/descendant::input
${preferred_language}    //p[text()='English']
${first_symptom_date}    //span[contains(text(),'When was the last day ')]/following::div[1]//input[@type='text']
${submit_form}     //button[@type='submit' and @class='submit btn btn-primary']
${success_message}    //p[text()='Form successfully saved!']


${app_home}    xpath://ol//li[contains(.,"NY-CDCMS: Web Apps Testing POC")]
${contacts_unassigned_open_menu}    (//div[@aria-label='All Contacts: Unassigned & Open']/div)[1]
${search_case}    id:searchText
${search_button}    id:case-list-search-button    
${contact_monitoring_form}    xpath://tr[@aria-label="Contact Monitoring"]
${initial_interview_disposition}    //p[text()='Reached person, agreed to call']
${final_disposition2}    //p[text()='Reached, completed investigation']
${symptom_fever}    //p[text()='Fever (subjective or measured)']
${symptom_fatigue}    //p[text()='Fatigue']
${symptom_congestion}    //p[text()='Congestion']
${symptom_runny_nose}    //p[text()='Runny nose']
${date_of_symptomp_onset}    //span[contains(text(),'date of onset')]/following::div[1]//input[@type='text']
${gender}    //p[text()='Female']
${race}    //p[text()='Asian']
${ethnicity}    //p[text()='Hispanic/Latino']
${yes_convert_pui}    //p[text()='Yes, convert contact/traveler to PUI']
${pui_form_header}    //h1[text()='Convert Contact to a Suspected Case (PUI)' and @class='title']
${confirm_yes_convert_pui}    //p[text()='Yes']   
${covert_to_pui_form}    //tr[@aria-label='Convert Contact to a Suspected Case (PUI)']

${all_suspected_cases_menu}    (//div[@aria-label='All Suspected Cases (PUIs)']/div)[1]
${webapps_home}    //a[@href="/a/ush-poc/cloudcare/apps/v2/" and @class="navbar-brand"]
${check_in_menu}   (//div[@aria-label='Check In']/div)[1] 
${search all cases}    //button[text()='Search All Cases']
${case search submit}    //button[@id='query-submit-button']
${change pui status form}    //tr[@aria-label='Change PUI Status']
${convert_back_to_contact}    //p[contains(.,'Convert this Suspected Case back to being a Contact')]
${are_you_sure}    //p[text()='Yes, convert this Suspected Case back into a Contact']
${close_record}    //p[text()="Yes"]
${dont_close_record}    //p[text()="No"]
${no_longer_active_message}    //strong[text()="This Suspected Case's contact record is no longer active, so you may not choose to convert it back to a contact."]
${close_yes_message}    //p[text()="The Suspected Case (PUI) will be closed, as will the associated contact record."]
${close_yes_message2}    //strong[text()="In order for the contact to be monitored again, the Contact Tracing team must re-open their record."]
${close_no_message}    //p[text()="This Suspected Case (PUI) will be converted back to being a contact. The Contact Tracing team will resume monitoring of this patient."]
${close_no_message2}    //strong[text()="To undo this action, a Contact Tracer will need to convert the Contact back into a PUI"]
${final_disposition}    //p[text()='Follow up completed']
${ send the release from quarantine notice by mail question}    //span[text()='Do you want to send the release from quarantine notice by mail?']
${date_notice_sent}    //span[text()='Date notice was sent by mail']
${send quarantine mail no}    //span[text()='Do you want to send the release from quarantine notice by mail?']/following::p[text()='No']
${send quarantine mail yes}    //span[text()='Do you want to send the release from quarantine notice by mail?']/following::p[text()='Yes']
${no notice label}    //span[text()="No notice will be sent"]

${like to send mail no}    //span[text()='Would you like to send the quarantine release notice by email?']/following::p[text()='No']
${like to send mail yes}    //span[text()='Would you like to send the quarantine release notice by email?']/following::p[text()='Yes']
${what_address}    xpath:(//span[text()='What email address should the notice be sent to']/following::textarea)[1]
${email_input}    test@test.in
${mail_label}    xpath://p/strong[text() = '${email_input}']


${all_closed_contacts_menu}   (//div[@aria-label='All Closed Contacts']/div)[1]
${all_open_contacts_menu}    (//div[@aria-label='All Open Contacts']/div)[1]
${archieved_contact}    xpath://td[text()='${archieved_contact_name}']

${sync}    xpath://div[@class='js-sync-item appicon appicon-sync']
${sync success}    xpath:(//div[text()='User Data successfully synced.'])[last()]
${first-name_case_search}    xpath:(//td/div[contains(., "First Name")]/following::input)[1]
