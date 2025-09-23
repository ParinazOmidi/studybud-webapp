def createRoom(request): 
    print("View called!")  # Debug print

    if request.method == 'POST': 
            print("POST request")  # Debug print
            form = RoomForm(request.POST)
            if form.is_valid(): 
                print("Form is valid")  # Debug print
                form.save()
                return redirect("home")
            else:
                print("Form errors:", form.errors)  # Debug print
    else:
            print("GET request")  # Debug print
            form = RoomForm()
        
            context = {'form': form}
            return render(request, 'playground/room_form.html', context)
    #   except Exception as e:
    #    print("Error:", str(e))  # Debug print
    #    raise e