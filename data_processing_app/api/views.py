import pandas as pd
from rest_framework.response import Response
from rest_framework.decorators import api_view

from data_processing_app.utils import infer_and_convert_data_types

@api_view(['POST'])
def process_data_view(request):
    try:
        uploaded_file = request.FILES['file']
        
        # Read the uploaded file into a DataFrame
        df = pd.read_csv(uploaded_file)
        
        # Process the data types using the utility function
        processed_df = infer_and_convert_data_types(df)
        
        # Convert the processed DataFrame to a dictionary
        processed_data = processed_df.to_dict(orient='records')
        
        return Response(processed_data)
    except Exception as e:
        return Response({'error': str(e)})
