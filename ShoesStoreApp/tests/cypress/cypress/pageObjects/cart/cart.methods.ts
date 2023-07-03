import {CartElements} from "./cart.elements";

export class CartMethods {
    increaseQuantity() {
        CartElements.ElementsCart.getIncreaseQuantityButton().first().click();
    }

    decreaseQuantity() {
        CartElements.ElementsCart.getDecreaseQuantityButton().first().click();
    }

    deleteOrderItem() {
        CartElements.ElementsCart.getDeleteOrderItemButton().click();
    }

    verifyShoesQuantity(number: number) {
        CartElements.ElementsCart.getItemQuantity().invoke('text').should('equal', String(number));
    }

    verifyDeleteButtonsCount(number: number) {
        CartElements.ElementsCart.getDeleteOrderItemButton().its('length').should('equal', number);
    }

    verifyFirstOrderItemPriceFor() {
        CartElements.ElementsCart.getItemQuantity().invoke('text').then(quantityText => {
            const quantity = parseInt(quantityText);
            CartElements.ElementsCart.getPrice().first().invoke('text').then(priceText => {
                const price = parseFloat(priceText.replace('$', ''));
                CartElements.ElementsCart.getOrderItemPrice().first().invoke('text').then(orderItemPriceText => {
                    const orderItemPrice = parseFloat(orderItemPriceText.replace('$', ''));
                    const expectedOrderItemPrice = price * quantity;
                    expect(orderItemPrice).to.equal(expectedOrderItemPrice);
                });
            });
        });
    }

    verifyTotalOrderPrice() {
        const total_order_price = CartElements.ElementsCart.getOrderPrice();
        let total_price = 0;

        CartElements.ElementsCart.getOrderItemPrice().each(($price) => {
            cy.wrap($price).invoke('text').then((text) => {
                const price = parseFloat(text.replace('$', ''));
                total_price += price;
            });
        }).then(() => {
            total_order_price.invoke('text').then((orderPriceText) => {
                const orderPrice = parseFloat(orderPriceText.replace('$', ''));
                const roundedTotalPrice = Math.round(total_price * 100) / 100;

                expect(roundedTotalPrice).to.equal(orderPrice);
            });
        });
    }
}