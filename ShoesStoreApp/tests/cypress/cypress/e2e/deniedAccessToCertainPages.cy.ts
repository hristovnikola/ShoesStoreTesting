import {ShoesMethods} from "../pageObjects/shoes/shoes.methods";
import {IndexMethods} from "../pageObjects/index/index.methods";

describe('User should not see this page', () => {
    let index = new IndexMethods();
    const testData = require('../fixtures/denied_access.json')
    testData.deniedAccess.forEach((testcase: { url: string }) => {
        it('User should not see the page: ' + testcase.url , () => {
            index.navigateToCertainPage(testcase.url);
            cy.url().should('include', '/loginPage');
        })
    });
})