developer_likes_and_dislikes = """

+------------------------------------+-----------------------------------+
| likes                              | dislikes                          |
+------------------------------------+-----------------------------------+
| Meritocracy                        | Favoritism, ass-kissing, politics |
+------------------------------------+-----------------------------------+
| Healthy debates and collaboration  | Ego-driven rhetoric, drama and FUD|
|                                    | to get one's way                  |
+------------------------------------+-----------------------------------+
| Autonomy given by confident leaders| Micro-management by insecure      |
| capable of attracting top-tier     | managers compensating for a weak, |
| talent                             | immature team                     |
+------------------------------------+-----------------------------------+
| Fluid communication, brief, ad-hoc | Formal meetings, endless debate   |
| discussions, white-boarding, and   |                                   |
| quick but informed decisions       |                                   |
+------------------------------------+-----------------------------------+
| Where else can I help out?         | I'm blocked by..., I only know how|
|                                    | to...                             |
+------------------------------------+-----------------------------------+
| Getting things done.               | Contrived company culture         |
+------------------------------------+-----------------------------------+
| Clever and disruptive business     |                                   |
| ideas that solve real and immediate|                                   |
| needs in a marketplace             |                                   |
+------------------------------------+-----------------------------------+
| Software and system abstractions   | Hard-coding, brute-force          |
+------------------------------------+-----------------------------------+
| Frameworks and best-practices      | Hermetic code-base                |
+------------------------------------+-----------------------------------+
| Best tool for the job              | One size fits all                 |
+------------------------------------+-----------------------------------+
| Simple design                      | Over-engineering                  |
+------------------------------------+-----------------------------------+
| Leveraging open-source             | Re-inventing the wheel            |
+------------------------------------+-----------------------------------+
| Practical solutions to business    | Let's do this or use that because |
| core competency                    | it's new and cool                 |
+------------------------------------+-----------------------------------+
| Building solutions to current      | Over-emphasizing "nice-to-haves"  |
| business needs and customer demand | and conjecture                    |
+------------------------------------+-----------------------------------+

"""

def string_parse(text):
    print 'string_parse:  text = %s' % (text)
    lines = text.split('\n')
    print 'string_parse:  lines = %s' % (lines)
    lines2 = [[str(s).strip() for s in l.split('|')] for l in lines]
    for s in lines2:
        print 'DEBUG.0: ',s

    lines3 = []
    for s in lines2:
        if (len(s) > 1) or (s[0].find('+-') > -1):
            if (len(s[0]) == 0) and (len(s[-1]) == 0):
                s = s[1:-1]
            if (s[0].lower() == 'likes') and (s[-1].lower() == 'dislikes'):
                continue
            lines3.append(s)

    print '='*80
    for s in lines3:
        print 'DEBUG.1: ',s

    lines4 = []
    num = 0
    cnt = len(lines3)
    while (num < cnt):
        s1 = lines3[num]
        if (num+1 < cnt):
            s2 = lines3[num+1]
            while ( (s1[0].find('+-') == -1) and (s2[0].find('+-') == -1) ):
                for n in xrange(0, len(s1)):
                    s1[n] = s1[n]+' '+s2[n]
                del lines3[num+1]
                cnt = len(lines3)
                s2 = lines3[num+1]
        if (s1[0].find('+-') > -1):
            num += 1
            continue
        lines4.append(s1)
        num += 1

    print '='*80
    for s in lines4:
        print 'DEBUG.3: ',s
    return lines4

print string_parse(developer_likes_and_dislikes)
