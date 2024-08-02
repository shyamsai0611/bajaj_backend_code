from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Details
from .serializers import DetailsSerializer

@api_view(['GET', 'POST'])
def details_view(request):
    if request.method == 'POST':
        data = request.data.get('data', [])
        user_id = "Shyam Sai "
        email = "shyamsaimanohar_k@srmap.edu.in"
        roll_number = "AP21110011197"
        numbers = [item for item in data if item.isdigit()]
        alphabets = [item for item in data if item.isalpha()]
        highest_alphabet = [max(alphabets)] if alphabets else []
        details_data = {
            'Status': True, 
            'User_id': user_id,
            'Email_id': email,
            'roll': roll_number,
            'numbers': numbers,
            'alphabets': alphabets,
            'highest_alphabet': highest_alphabet
        }
        serializer = DetailsSerializer(data=details_data)
        if serializer.is_valid():
            serializer.save()
            response_data = {
                "is_success": True,
                "user_id": user_id,
                "email": email,
                "roll_number": roll_number,
                "numbers": numbers,
                "alphabets": alphabets,
                "highest_alphabet": highest_alphabet
            }
            return Response(response_data, status=201)
        return Response(serializer.errors, status=400)

    else:
        details = Details.objects.all()
        serializer = DetailsSerializer(details, many=True)
        return Response(serializer.data)
