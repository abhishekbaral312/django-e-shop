from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from store.models.customer import Customer
from django.views import View


class SignUp(View):
    def get(self, request):
        return render(request, 'signup.html')

    def post(self, request):
        postData = request.POST
        first_name = postData.get('firstname')
        last_name = postData.get('lastname')
        phone = postData.get('phone')
        email = postData.get('email')
        password = postData.get('password')

        # validation
        value = {
            'first_name': first_name,
            'last_name': last_name,
            'phone': phone,
            'email': email
        }
        error_message = None

        customer = Customer(first_name=first_name,
                            last_name=last_name,
                            phone=phone,
                            email=email,
                            password=password)

        error_message = self.validateCustomer(customer)

        # saving
        if not error_message:
            customer.password = make_password(customer.password)

            customer.register()

            return redirect('homepage')
        else:
            data = {
                'error': error_message,
                'values': value
            }
            return render(request, 'signup.html', data)

    def validateCustomer(self, customer):
        error_message = None;
        if (not customer.first_name):
            error_message = "First Name required !!"
        elif len(customer.first_name) < 4:
            error_message = "First Name Must be 4 char long or more"
        elif (not customer.last_name):
            error_message = "Last Name required !!"
        elif len(customer.last_name) < 1:
            error_message = "Last Name Must be 4 char long or more"
        elif (not customer.phone):
            error_message = "phone number required !!"
        elif len(customer.phone) < 10:
            error_message = "phone number Must be of 10 number"
        elif (not customer.email):
            error_message = "email required !!"
        elif (not customer.password):
            error_message = "password required !!"
        elif len(customer.password) < 8:
            error_message = "password Must be 8 char long or more"
        elif customer.isExists():
            error_message = "Email Address Already Registered"
        elif customer.isExistspass():
            error_message = "Phone Number Already Registered"
        return error_message
