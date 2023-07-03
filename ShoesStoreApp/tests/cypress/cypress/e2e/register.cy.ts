import {RegisterMethods} from "../pageObjects/register/register.methods";
import {LoginMethods} from "../pageObjects/login/login.methods";
import {IndexMethods} from "../pageObjects/index/index.methods";

describe('Register Cypress test', () => {
    let login = new LoginMethods();
    let register = new RegisterMethods()
    let index = new IndexMethods()
    const testDataLogin = require('../fixtures/new_login.json')
    const testDataRegister = require('../fixtures/register.json')

    beforeEach(function () {
        index.navigateToIndexPage('http://localhost:8000/index/');
        login.navigateToLoginPage();
    })

    // Trying to log in when the user is not register (Should not be able to login)
    testDataLogin.newLoginData.forEach((testcase: { username: string; password: string; }) => {
        it(testcase.username + ' should not be able to login', () => {
            login.login(testcase.username, testcase.password);
            login.verifyUsernameDoesNotExistsOnPage(testcase.username);
        })
    });

    // The user is registering
    testDataRegister.registerData.forEach((testcase: {
        username: string;
        email: string;
        password: string;
        repeat_password: string
    }) => {
        it(testcase.username + ' should be able to register', () => {
            register.navigateToRegisterPage();
            register.register(testcase.username, testcase.email, testcase.password, testcase.repeat_password);
        })
    });

    // The user is logging in
    testDataLogin.newLoginData.forEach((testcase: { username: string; password: string; }) => {
        it(testcase.username + ' should be able to login', () => {
            login.login(testcase.username, testcase.password);
            login.verifyUsernameExistsOnPage(testcase.username);
        })
    });
})