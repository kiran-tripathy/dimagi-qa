/// <reference types="cypress" />
import locator from '../../fixtures/locators.json';

class logInPage {
    visit(value) {
      cy.visit(value);
    }
  
    fillEmail(value) {
      const field = cy.get(locator.loginPage.username);
      field.clear();
      field.type(value);
  
      return this;
    }


    acceptCookie() {
        const field = cy.get(locator.loginPage.cookie, {timeout: 20000});
          field.click();
      }
     
      clickContinue() {
        const field = cy.get(locator.loginPage.continue);
        field.click()
        }

  
    fillPassword(value) {
      const field = cy.get(locator.loginPage.password);
      field.clear();
      field.type(value);
  
      return this;
    }
  

    submit() {
      const button = cy.get(locator.loginPage.submit);
      button.click();
    }
  }
  
  export default logInPage;