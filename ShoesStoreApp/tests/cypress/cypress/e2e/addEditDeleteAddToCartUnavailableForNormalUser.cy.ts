import {ShoesMethods} from "../pageObjects/shoes/shoes.methods";
import {IndexMethods} from "../pageObjects/index/index.methods";

describe('Unauthenticated user tests', () => {
    let index = new IndexMethods();
    let shoes = new ShoesMethods();
    beforeEach(function () {
        index.navigateToIndexPage('http://localhost:8000/index/');
        shoes.navigateToShoesPage();
    })

    it('Unauthenticated user should not see "Add Shoes" button', function () {
        shoes.verifyAddShoesDoesNotExist();
    });

    it('Unauthenticated user should not see "Add to cart", "Edit" and "Delete" buttons, but should see "Back to shoes" button', function () {
        shoes.navigateToShoesDetailsPage();
        shoes.verifyEditDeleteAddToCartDoNotExist();
        shoes.verifyBackToShoesExist();
    });
})