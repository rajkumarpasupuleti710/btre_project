from django.shortcuts import render, redirect
from django.contrib  import messages
from django.core.mail import send_mail
from .models import Contact
def contact(request):
    if request.method == "POST":
        listing_id = request.POST['listing_id']
        listing = request.POST['listing']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        user_id = request.POST['user_id']
        realtor_email = request.POST['realtor_email']

        #check if user has made inquiry already
        if request.user.is_authenticated:
            has_contacted=Contact.objects.all().filter(listing_id=listing_id, user_id=user_id)
            if has_contacted:
                messages.error(request,"You have enquired on this property before")
                return redirect("/listings/"+listing_id) 

        contact=Contact(listing=listing,listing_id=listing_id,name=name,email=email,phone=phone,message=message,user_id=user_id)

        contact.save()
        
        #send email
        send_mail(
            'Propert Listing Inquiry',
            f'There has been an inquiry for {listing}. Sign into the admin panel for more info.',
            'rajkumarr7102002@gmail.com',
            [realtor_email],
            fail_silently=False
        )
        if request.user.is_authenticated:
            
            send_mail(
                'Propert Listing Inquiry',
                f'You have inquiried for {listing}. Sign into the website for more info.',
                'rajkumarr7102002@gmail.com',
                [email],
                fail_silently=False
            )


        messages.success(request,"Your request has been submitted, a realtor will get back to you soon")

        return redirect('/listings/'+listing_id)
