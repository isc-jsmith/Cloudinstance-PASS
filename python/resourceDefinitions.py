import datetime

#################################
#
# Define an Event Ticket Class
# See https://developers.google.com/pay/passes/reference/v1/eventticketclass
# @param String classId - The unique identifier for a class
# @return Dict payload - represents Event Ticket class resource
#
#################################

def makeEventTicketClassResource(classId, Globalname, Globalmrn, Globaldate, Globaldoctor, Globalhospital, Globalhospitalphone, Globalhospitaladdress, Globallocation, Globalservice):
  # Define the resource representation of the Class
  # values should be from your DB/services; here we hardcode information

  payload = {}

  # below defines an event ticket class. For more properties, check:
  # https://developers.google.com/pay/passes/reference/v1/eventticketclass/insert
  # https://developers.google.com/pay/passes/guides/pass-verticals/event-tickets/design

  payload = {
    # required fields
    "id": classId
    ,"issuerName": "Appointment Confirmation"
    ,"eventName": {
      "defaultValue": {
        "language": "en-US",
        "value": "Appointment for "+Globalname
      }
    }
    ,"reviewStatus": "underReview"
    # optional
    ,"locations": [{
        "kind": "walletobjects#latLongPoint"
        ,"latitude": 37.424015499999996
        ,"longitude": -122.09259560000001
    }]
    ,"review": {
        "comments": "Real auto approval by system"
    }
    ,"textModulesData": [{
        "header": "Custom Details"
        ,"body": "Dear "+Globalname+",\nOur Records show that you have an appointment on "+Globaldate+" with "+Globaldoctor+" at "+Globalhospital+", "+Globallocation+" in regards to "+Globalservice+"\nPlease ensure that you bring all the required documents to your appointment."
    }]
    ,"linksModuleData": {
        "uris": [ {
            "kind": "walletobjects#uri"
            ,"uri": "tel:"+str(Globalhospitalphone)
            ,"description": "Call "+Globalhospital
        }]
    }
    ,"imageModulesData": [{
        "mainImage": {
            "kind": "walletobjects#image"
            ,"sourceUri": {
                "kind": "walletobjects#uri"
                ,"uri": "https://i.postimg.cc/vTc5wjq6/medical-563427-640.jpg"
                ,"description": "Steth"
            }
        }
    }],
    "logo": {
        "kind": "walletobjects#image"
          ,"sourceUri": {
            "kind": "walletobjects#uri"
            ,"uri": "https://i.postimg.cc/DwTmr0VM/appt.jpg"
            ,"description": "logo"
        }
    }
    ,"venue": {
        "kind": "walletobjects#eventVenue"
          ,"name": {
            "kind": "walletobjects#localizedString"
            ,"defaultValue": {
              "kind": "walletobjects#translatedString"
              ,"language": "en-us"
              ,"value": " "+Globalhospital+" - "+Globallocation
            }
        },
          "address": {
            "kind": "walletobjects#localizedString"
            ,"defaultValue": {
              "kind": "walletobjects#translatedString"
              ,"language": "en-us"
              ,"value": " "+Globalhospitaladdress
            }
        }
    }
    ,"dateTime": {
      "kind": "walletobjects#eventDateTime"
      ,"Date & Time": ""+Globaldate
      
    }
  }
  return payload



##################################
#
# Define an Event Ticket Object
# See https://developers.google.com/pay/passes/reference/v1/eventticketobject
# @param String classId - The unique identifier for a class
# @param String objectId - The unique identifier for an object
# @return Dict payload - represents Event Ticket object resource
#
#################################
def makeEventTicketObjectResource(classId, objectId, Globalname, Globalmrn, Globaldate, Globaldoctor, Globalhospital, Globallocation, Globalservice):
  # Define the resource representation of the Object
  # values should be from your DB/services; here we hardcode information

  payload = {}

  # below defines an event ticket object. For more properties, check:
  # https://developers.google.com/pay/passes/reference/v1/eventticketobject/insert
  # https://developers.google.com/pay/passes/guides/pass-verticals/event-tickets/design

  payload = {
    # required fields
    "id" : objectId
    ,"classId" : classId
    ,"state" : "active"
    # optional
    ,"barcode": {
      "kind": "walletobjects#barcode"
      ,"type": "code39"
      ,"value": ""+Globalmrn
      ,"alternateText": "MRN barcode "+Globalmrn
    }
    ,"seatInfo": {
        "kind": "walletobjects#eventSeat"
        ,"seat": {
            "kind": "walletobjects#localizedString"
            ,"defaultValue": {
                "kind": "walletobjects#translatedString",
                "language": "en-us",
                "value": " "+Globalservice
            }
        }
        ,"row": {
            "kind": "walletobjects#localizedString"
            ,"defaultValue": {
                "kind": "walletobjects#translatedString"
                ,"language": "en-us"
                ,"value": "In regards to"
            }
        }
        ,"section": {
            "kind": "walletobjects#localizedString"
            ,"defaultValue": {
                "kind": "walletobjects#translatedString"
                ,"language": "en-us"
                ,"value": ""+Globaldoctor
            }
        }
        ,"gate": {
            "kind": "walletobjects#localizedString"
            ,"defaultValue": {
                "kind": "walletobjects#translatedString"
                ,"language": "en-us"
                ,"value": ""+Globaldate
            }
        }
    }
    #,"Name": ""
    #,"ticketNumber": "123abc"
  }

  return payload



