import {ShoesMethods} from "../pageObjects/shoes/shoes.methods";
import {IndexMethods} from "../pageObjects/index/index.methods";
import {LoginMethods} from "../pageObjects/login/login.methods";

describe('Admin adds shoes, edits them and then deletes them', () => {
    let index = new IndexMethods();
    let login = new LoginMethods();
    let shoes = new ShoesMethods();
    const testData = require('../fixtures/add_shoes.json')

    beforeEach(function () {
        index.navigateToIndexPage('http://localhost:8000/index/');
        login.navigateToLoginPage();
        login.login("admin", "dnick201097homework");
        shoes.navigateToShoesPage();
    })

    testData.addNewShoes.forEach((testcase: {
        name: string;
        price: string;
        description: string;
        available_size: string;
        brand: string;
        type: string;
        color: string;
        image: string;
    }) => {
        it('Admin should be able to add new shoes', function () {
            shoes.verifyAddShoesDoesExist();
            shoes.addNewShoesToList(testcase.name, testcase.price, testcase.description, testcase.available_size,
                testcase.brand, testcase.type, testcase.color, testcase.image);
            cy.get('body').invoke('text').should('contain', testcase.name)
        });

        it('Admin should be able to edit the recently added shoes', function () {
             shoes.editRecentlyAddedShoes(testcase.name);
             cy.get('body').invoke('text').should('contain', 'AAA');
        });

        it('Admin should be able to edit the recently added and edited shoes', function () {
            shoes.deleteRecentlyAddedShoes('AAA');
        });
    })
})