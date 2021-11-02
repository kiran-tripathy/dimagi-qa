/// <reference types="cypress" />

import loginPage from '../pageObjects/loginPage'
import webappsPage from '../pageObjects/webappsPage'
import data from '../../fixtures/userdata.json';
import locator from '../../fixtures/locators.json';


describe('Formplayer Tests', function() {

    before('Login',() => { 
        const lp=new loginPage
        lp.visit(Cypress.env('QA_URL'))
        lp.fillEmail(Cypress.env('LOGIN_USERNAME'))
        lp.clickContinue()
        lp.acceptCookie()
        lp.fillPassword(Cypress.env('LOGIN_PASSWORD'))
        lp.submit()
        cy.title().should('be.equal', 'CommCare HQ')})
    
    it('Open webapps and Login As', function() {        
        const lw=new webappsPage
        lw.openWebapps()
        lw.loginAs()
        cy.get(locator.test_01_spec.restore_as_banner)
        .should('contain.text', 'Working as test')
        .and('be.visible')
    })
    
    it('Submit form as mobile worker', function() {    
        const sf=new webappsPage
        sf.submitForm(data.name)
        cy.get(locator.test_01_spec.success_msg)
        .should('be.visible')
        .and('contain.text', 'Form successfully saved!')
    })

    it('Submit form as webuser', function() {    
        const sf=new webappsPage
        sf.loginasWebUser()
        sf.submitForm(data.name)
        cy.get(locator.test_01_spec.success_msg)
        .should('be.visible')
        .and('contain.text', 'Form successfully saved!')
    })
})

