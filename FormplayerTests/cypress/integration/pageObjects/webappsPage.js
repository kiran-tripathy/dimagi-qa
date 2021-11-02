/// <reference types="cypress" />
import locator from '../../fixtures/locators.json';

class webappsPage {

    openWebapps() {
        const menu = cy.get(locator.webappsPage.webapps_menu);
        menu.click()
      }
  
    loginAs() {
        const loginas = cy.get(locator.webappsPage.loginas)
        loginas.click()
        const user = cy.get(locator.webappsPage.loginas_user)
        user.click();
        const confirm = cy.get(locator.webappsPage.confirm_user)
        confirm.click();      
    }
    
    submitForm(data){
      const selectapp = cy.xpath(locator.webappsPage.select_basic_tests_app)
      selectapp.click()
      const selectmenu = cy.get(locator.webappsPage.select_basic_tests_menu);
      selectmenu.click();
      const openform = cy.get(locator.webappsPage.open_basic_tests_form)
      openform.click()
      const enterdata = cy.xpath(locator.webappsPage.basic_test_data_field)
      enterdata.type(data);

      const submit = cy.get(locator.webappsPage.submit_form)
      submit.click()
      return this;          
      }

    loginasWebUser(){
      const loginaswebuser = cy.xpath(locator.webappsPage.login_as_webuser)
      loginaswebuser.click()
    }
      
    }

  
  export default webappsPage;