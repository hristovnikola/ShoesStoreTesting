import {ShoesMethods} from "../pageObjects/shoes/shoes.methods";
import {IndexMethods} from "../pageObjects/index/index.methods";
import {LoginMethods} from "../pageObjects/login/login.methods";
import {CartMethods} from "../pageObjects/cart/cart.methods";

describe('Customer adds shoes to cart, increases and decreases quantitiy of the order item, deletes order item', () => {
    let index = new IndexMethods();
    let login = new LoginMethods();
    let shoes = new ShoesMethods();
    let cart = new CartMethods();
    const testData = require('../fixtures/add_shoes.json')

    beforeEach(function () {
        index.navigateToIndexPage('http://localhost:8000/index/');
        login.navigateToLoginPage();
        login.login("hristov.nikola", "customerpass");
        shoes.navigateToShoesPage();
    })

    it('Customer should be able to add shoes in cart, change quantity, delete order item and go to the checkout page', function () {
        shoes.navigateToShoesDetailsPage();
        shoes.selectSizeForShoes();
        shoes.clickOnAddToCartButton();
        for (let i = 0; i < 3; i++) {
            cart.increaseQuantity(); // Call the function multiple times
        }
        cart.decreaseQuantity();
        cart.verifyShoesQuantity(3);
        cart.verifyFirstOrderItemPriceFor();
        shoes.navigateToShoesPage();
        shoes.navigateSpecificShoesDetailsPage(1);
        shoes.selectSizeForShoes();
        shoes.clickOnAddToCartButton();
        cart.verifyDeleteButtonsCount(2);
        cart.verifyTotalOrderPrice()
    });

})