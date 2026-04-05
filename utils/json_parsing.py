import json
ai_response= """
{
    "title":"Harry Potter and the Sorcerer's Stone",
    "author":"J.K. Rowling",
    "published_year": 1997    
}
"""

book_data=json.loads(ai_response)
print(book_data)