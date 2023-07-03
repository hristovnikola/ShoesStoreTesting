import {ShoesElements} from "./shoes.elements";
import {LoginElements} from "../login/login.elements";
import {CartElements} from "../cart/cart.elements";

export class ShoesMethods {
    navigateToShoesPage() {
        ShoesElements.ElementsShoes.getShoesNavButton().click();
    }

    navigateToShoesDetailsPage() {
        ShoesElements.ElementsShoes.getDetailsButtons().first().click();
    }

    navigateSpecificShoesDetailsPage(number: number) {
        ShoesElements.ElementsShoes.getDetailsButtons().eq(number).click();
    }

    addNewShoesToList(name: string, price: string, description: string, available_size: string, brand: string, type: string, color: string, image: string) {
        ShoesElements.ElementsShoes.getAddShoesButton().click();
        ShoesElements.AddAndEditShoesElements.getNameField().type(name);
        ShoesElements.AddAndEditShoesElements.getPriceField().type(price);
        ShoesElements.AddAndEditShoesElements.getDescriptionField().type(description);
        ShoesElements.AddAndEditShoesElements.getAvailableSizesField().select(available_size);
        ShoesElements.AddAndEditShoesElements.getBrandField().select(brand);
        ShoesElements.AddAndEditShoesElements.getTypeField().select(type);
        ShoesElements.AddAndEditShoesElements.getColorField().type(color);
        ShoesElements.AddAndEditShoesElements.getImageField().selectFile(image);
        ShoesElements.AddAndEditShoesElements.getSubmitAddingOrEditingShoesButton().click()
    }

    editRecentlyAddedShoes(name: string) {
        cy.contains(name).parent().find('.details_button').click();
        ShoesElements.ElementsShoes.getEditButton().click();
        ShoesElements.AddAndEditShoesElements.getNameField().clear().type('AAA');
        ShoesElements.AddAndEditShoesElements.getPriceField().clear().type('55');
        ShoesElements.AddAndEditShoesElements.getDescriptionField().clear().type('Edited Description');
        ShoesElements.AddAndEditShoesElements.getSubmitAddingOrEditingShoesButton().click();
    }

    deleteRecentlyAddedShoes(name: string) {
        cy.contains(name).parent().find('.details_button').click();
        ShoesElements.ElementsShoes.getDeleteButton().click();
        ShoesElements.ElementsShoes.getBodyText().should('not.contain', name);
    }

    selectSizeForShoes() {
        ShoesElements.ElementsShoes.getShoesSizeInput().first().check();
    }

    clickOnAddToCartButton() {
        ShoesElements.ElementsShoes.getAddToCartButton().click();
    }

    verifyEditDeleteAddToCartDoNotExist() {
        ShoesElements.ElementsShoes.getEditButton().should('not.exist');
        ShoesElements.ElementsShoes.getDeleteButton().should('not.exist');
        ShoesElements.ElementsShoes.getAddToCartButton().should('not.exist');
    }

    verifyBackToShoesExist() {
        ShoesElements.ElementsShoes.getBackToShoesButton().should('exist').click();
    }

    verifyAddShoesDoesExist() {
        ShoesElements.ElementsShoes.getAddShoesButton().should('exist');
    }

    verifyAddShoesDoesNotExist() {
        ShoesElements.ElementsShoes.getAddShoesButton().should('not.exist');
    }

}