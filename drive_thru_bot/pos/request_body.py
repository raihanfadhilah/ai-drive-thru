TEMPLATE = {
    "additionalReferenceIds": {"someRefID": "myCustomReferenceID"},
    "bagCount": 4,
    "channel": "Web",
    "checkInDetails": {
        "application": "POS",
        "location": "Drive Thru",
        "origin": {"id": 12, "type": "web"},
        "vector": {"id": 75, "type": "terminal"},
    },
    "comments": "A comment left on the order",
    "currency": "AED",
    "customer": {
        "email": "ruben.bear@ncr.com",
        "externalIds": [
            {
                "lineId": "ruben-1",
                "type": "Loyalty",
                "value": "A member of the loyalty program",
            }
        ],
        "firstName": "Ruben",
        "fiscalId": "ruben-fiscal-identification",
        "id": "ruben-identification",
        "lastName": "The Bear",
        "name": "Ruben The Bear",
        "phone": "123-456-7890",
    },
    "errorDescription": "No error.",
    "fees": [],
    "fulfillment": {
        "address": {
            "businessInfo": {"department": "Devex", "name": "NCR"},
            "city": "Atlanta",
            "coordinates": {"latitude": 33.6817952, "longitude": -84.4239568},
            "country": "United States of America",
            "crossStreets": [{"name": "Peachtree St"}],
            "line1": "864 Peachtree St",
            "notes": "Please deliver to Ruben The Bear!",
            "postalCode": "30308",
            "state": "Georgia",
            "type": "Business",
        },
        "autoRelease": False,
        "catering": True,
        "leadTimes": [{"interval": 83, "intervalUnits": "Minutes", "type": "Transit"}],
        "notes": "Please deliver to Ruben The Bear",
        "type": "Delivery",
    },
    "orderLines": [
        {
            "description": "The description of the order line",
            "extendedAmount": 20.8,
            "fulfillmentResult": "Fulfilled",
            "itemType": "Tare",
            "linkGroupCode": "Hospitality-Link-Group-Code",
            "modifierCode": "well done",
            "notes": [
                {"type": "Substitutions", "value": "Lightly salted"},
                {"type": "Preferences", "value": "No pickles"},
            ],
            "overridePrice": True,
            "priceModifiers": [{"amount": 1.99, "description": "Extra Cheese"}],
            "productId": {"type": "UPC", "value": "Cheeseburger"},
            "quantity": {
                "unitOfMeasure": "EA",
                "unitOfMeasureLabel": "lbs",
                "value": 78.55,
            },
            "scanData": "Any data that pertains to a POS that scans a bar code",
            "substitutionAllowed": True,
            "supplementalData": "Any supplemental data that pertains to an order",
            "taxes": [
                {
                    "amount": 92.85,
                    "code": "Sales-Tax",
                    "isIncluded": True,
                    "percentage": 0.07,
                }
            ],
            "unitPrice": 26.5,
        }
    ],
    "owner": "Ruben's Hamburger Hut",
    "partySize": 1,
    "payments": [
        {
            "accountNumber": "12345678901234",
            "amount": 42.1,
            "description": "A description for the payment",
            "expiration": {"month": 11, "year": 2031},
            "gratuity": 48.35,
            "payBalance": True,
            "status": "Authorized",
            "type": "Cash",
        }
    ],
    "pickupContact": {
        "company": "NCR",
        "hasArrived": False,
        "name": "Ruben",
        "phone": "123-456-7890",
        "vehicle": {
            "color": "Silver",
            "licensePlate": "ABC1234",
            "make": "Porsche",
            "model": "911 Turbo",
            "year": "2017",
        },
    },
    "promotions": [
        {
            "adjustment": {"applied": None, "level": "ITEM", "type": "PROMO"},
            "amount": 50.25,
            "numGuests": 97,
            "orderLineGroups": [
                {
                    "name": "Name of an order line group",
                    "orderLineIds": ["order-line-id"],
                }
            ],
            "supportingData": "Any extra supporting data of the promotion",
        }
    ],
    "revenueCenter": "bar",
    "status": "OrderPlaced",
    "taxExempt": False,
    "taxes": [
        {
            "active": True,
            "amount": 6.4,
            "code": "Servoce",
            "description": "Service tax",
            "isIncluded": False,
            "percentage": 52.4,
        }
    ],
    "totals": [{"type": "Net", "value": 27.45}],
}
