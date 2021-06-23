
import json

from biblebooks import idx2books, getBookName, books2idx, wholebible_book_iterator, numchaps

def lambda_handler(event, context):
    eventbody = json.loads(event['body'])

    query = eventbody['query']
    assert len(query.keys())
    response = {}
    if 'bookid' in query:
        bookid = query['bookid']
        response['bookid'] = bookid
        bookabbr = idx2books[bookid]
        response['bookabbr'] = bookabbr
        response['book'] = getBookName(bookabbr)
        response['nbchaps'] = numchaps[bookabbr]
    elif 'bookabbr' in query:
        bookabbr = query['bookabbr']
        response['bookabbr'] = bookabbr
        response['bookid'] = books2idx[bookabbr]
        response['book'] = getBookName(bookabbr)
        response['nbchaps'] = numchaps[bookabbr]
    elif 'book' in query:
        book = query['book']
        bookabbr = None
        for abbr in wholebible_book_iterator():
            if getBookName(abbr) == book:
                bookabbr = abbr
                break
        if bookabbr is None:
            raise ValueError('No such book in the Bible: {}'.format(book))
        response['book'] = book
        response['bookabbr'] = bookabbr
        response['bookid'] = books2idx[bookabbr]
        response['nbchaps'] = numchaps[bookabbr]
    else:
        raise ValueError('Invalid query.')

    return {
        'statusCode': 200,
        'body': json.dumps(response)
    }
