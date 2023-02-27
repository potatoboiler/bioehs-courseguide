from . import models

execIterable = ['President',
'External Vice President',
'Internal Vice President',
'Treasurer',
'Secretary',
'BioEHSC™ Senior Chair',
'BioEHSC™ External Relations Chair']

nonExecIterable = [
'BioEHSC™ Junior Chair',
'BioEHSC™ Junior Co-Chair',
'BDB DeCal Facilitator',
'Webmaster',
'Outreach Chair',
'Projects Chair',
'Academic Chair',
'Publicity Chair',
'Professional Development Chair',
'Historian',
'Co-Historian',
'Social Chair',
'Community Service Chair']

assistantOfficersIterable = ['External Vice President Assistant Officer', 'Internal Vice President Assistant Officer', 'Academic Assistant Officer',
'Outreach Assistant Officer',
'Professional Development Assistant Officer',
'Projects Assistant Officer', 'Treasurer Assistant Officer', 'BDB DeCal Assistant Facilitator']

advisorsIterable = ['Senior Advisor',
'Faculty Advisor']

def officerDetailHTML(officerRankIterable, semester):
    columns = 3
    counter = 0
    html = "<table class='table'><tbody>"
    for title in officerRankIterable:
        for pos in semester.positions.all():
            if pos.get_title_display() == title:
                for officer in pos.officers.all():
                    if (counter % columns) == 0:
                        if (counter // columns) > 0:
                            html += "</tr>"
                        html += "<tr>"
                    html += "<td style='width: 25%'><h5>{}</h5><h6>{}".format(title, officer.user.get_full_name())
                    if officer.linkedin:
                        html += "<a href='{}' target='_blank'><img src='https://cdn1.iconfinder.com/data/icons/logotypes/32/square-linkedin-512.png' style='width: 25px; margin-left: 5px;'alt='LinkedIn'></a>".format(officer.linkedin)
                    html += "</h6><img id='prof' class='zoom' src='{}'/></td>".format(officer.image.url)
                    counter += 1
    if (counter % columns) == 0:
        html += "</tr>"
    html += "</tbody></table>"
    return html

def alumniDetailHTML():
    html = ""
    for alum in models.UserProfile.userprofiles.filter(is_beacon_alumnus=True):
        html += "<hr><div class='row bordered'>"

        if alum.linkedin:
            html += "<div class='col-md-4'>"
            html += "<a href='#contact' data-cid='1' data-cname={} class='alumnus-link alumni-left'><div></div>\
            <script type='IN/MemberProfile' data-id={} data-format='inline'></script></a>".format(alum.user.get_full_name(), alum.linkedin)
            html += "<a href='{}' target='_blank'><img src='https://cdn1.iconfinder.com/data/icons/logotypes/32/square-linkedin-512.png' style='width: 25px; margin-left: 5px;'alt='LinkedIn'></a>".format(alum.linkedin)
            html += "</div><div class='col-md-8'>"
        else:
            html += "<div class='col-md-12'>"
        # html += "</h6><img id='prof' class='zoom' src='{}'/></td>".format(alum.image.url) need to re-position the images here
        html += "<h4>{}</h4>".format(alum.user.get_full_name())
        #if alum.alumnus_last_contacted:
            #html += "<h5>{}</h5>".format(alum.alumnus_last_contacted)
        if alum.beacon_bio:
            html += "<p>{}</p>".format(alum.beacon_bio)
        html += "</div></div>"
    return html
