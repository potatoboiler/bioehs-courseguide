from . import models

def sponsorDetailHTML(year):
    columns = 4
    counter = 0
    html = "<table class='table'><tbody>"
    for sponsor in year.sponsors.all():
        if (counter % columns) == 0:
            if (counter // columns) > 0:
                html += "</tr>"
            html += "<tr>"
        html += "<td style='width: 25%'>\
                <a href={} target='_blank'>\
                <div id='sponsor-container'>\
                <img class='zoom sponsor-logo' src='{}'/>\
                </div>\
                </a>\
                </td>".format(sponsor.link,  sponsor.pic.url)
        counter+=1
        if (counter % columns) == 0:
            html += "</tr>"
    html += "</tbody></table>"
    return html
