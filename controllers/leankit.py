import urllib2, base64, json
def dashboard():
    # url = 'https://atctrailers.leankit.com/kanban/api/board/199063443/Archive' # This gets the archive lane
    url = 'https://atctrailers.leankit.com/kanban/api/boards/199063443'  # This gets all lanes except archive
    username = 'aaronc@aluminumtrailer.com'
    password = '8v!Wr2S'

    request = urllib2.Request(url, headers={'User-Agent' : "Magic Browser"})
    base64string = base64.encodestring('%s:%s' % (username, password)).replace('\n', '')
    request.add_header("Authorization", "Basic %s" % base64string)
    try:
        result = urllib2.urlopen(request)
    except urllib2.HTTPError, e:
        error = e.fp.read()

    resultString = result.read()  # returns value as a string
    data = json.loads(resultString)  # converts to a json object

    replyData = data['ReplyData']
    lanes = replyData[0]['Lanes']
    count = 0
    response = []
    for lane in lanes:
        name = lane['Title']
        for cards in lane['Cards']:
            blocked = cards['IsBlocked']
            if blocked:
                cardName = cards['Title']
                reasonBlocked = cards['BlockReason']
                dateDue = cards['DueDate']
                cardId = cards['ExternalCardID']
                lastModified = cards['LastActivity']
                response.append({'Lane': name, 'Card ID': cardId, 'Card Name': cardName, 'Why Blocked': reasonBlocked, 'Date Due': dateDue, 'Last Modified': lastModified})
                count += 1
    blocked_table = HTML.table(response, header_row=['Lane',   'Card Id',   'Card Name', 'Reason','Due Date','Modified'])
# print json.dumps(response)
# print count

def stories():
    message = 'This is all active stories'