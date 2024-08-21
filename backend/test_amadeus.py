# test_amadeus_api.py  
import asyncio 
import httpx
from app.utils.amadus import AmadeusTravelAPIWrapper  
async def main():  
    api_wrapper = AmadeusTravelAPIWrapper()  
    
    endpoint = "/v1/booking/flight-orders"  
    method = "POST"  
    # body = {  
    #     "data": {  
    #         "type": "flight-order",  
    #         "flightOffers": [  
    #             {  
    #                 "type": "flight-offer",  
    #                 "id": "1",  
    #                 "source": "GDS",  
    #                 "instantTicketingRequired": False,  
    #                 "nonHomogeneous": False,  
    #                 "oneWay": False,  
    #                 "lastTicketingDate": "2024-08-10",  
    #                 "numberOfBookableSeats": 4,  
    #                 "itineraries": [  
    #                     {  
    #                         "duration": "PT17H5M",  
    #                         "segments": [  
    #                             {  
    #                                 "departure": {  
    #                                     "iataCode": "CDG",  
    #                                     "terminal": "2F",  
    #                                     "at": "2024-08-10T17:50:00"  
    #                                 },  
    #                                 "arrival": {  
    #                                     "iataCode": "AMS",  
    #                                     "at": "2024-08-10T19:15:00"  
    #                                 },  
    #                                 "carrierCode": "KL",  
    #                                 "number": "1234",  
    #                                 "aircraft": {  
    #                                     "code": "738"  
    #                                 },  
    #                                 "operating": {  
    #                                     "carrierCode": "KL"  
    #                                 }  
    #                             },  
    #                             {  
    #                                 "departure": {  
    #                                     "iataCode": "AMS",  
    #                                     "at": "2024-08-11T12:55:00"  
    #                                 },  
    #                                 "arrival": {  
    #                                     "iataCode": "PTY",  
    #                                     "at": "2024-08-11T16:50:00"  
    #                                 },  
    #                                 "carrierCode": "KL",  
    #                                 "number": "7890",  
    #                                 "aircraft": {  
    #                                     "code": "77W"  
    #                                 },  
    #                                 "operating": {  
    #                                     "carrierCode": "KL"  
    #                                 }  
    #                             },  
    #                             {  
    #                                 "departure": {  
    #                                     "iataCode": "PTY",  
    #                                     "at": "2024-08-12T11:57:00"  
    #                                 },  
    #                                 "arrival": {  
    #                                     "iataCode": "KIN",  
    #                                     "at": "2024-08-12T13:55:00"  
    #                                 },  
    #                                 "carrierCode": "CM",  
    #                                 "number": "4321",  
    #                                 "aircraft": {  
    #                                     "code": "738"  
    #                                 },  
    #                                 "operating": {  
    #                                     "carrierCode": "CM"  
    #                                 }  
    #                             }  
    #                         ]  
    #                     },  
    #                     {  
    #                         "duration": "PT13H35M",  
    #                         "segments": [  
    #                             {  
    #                                 "departure": {  
    #                                     "iataCode": "KIN",  
    #                                     "at": "2024-08-20T14:57:00"  
    #                                 },  
    #                                 "arrival": {  
    #                                     "iataCode": "PTY",  
    #                                     "at": "2024-08-20T17:05:00"  
    #                                 },  
    #                                 "carrierCode": "CM",  
    #                                 "number": "4321",  
    #                                 "aircraft": {  
    #                                     "code": "738"  
    #                                 },  
    #                                 "operating": {  
    #                                     "carrierCode": "CM"  
    #                                 }  
    #                             },  
    #                             {  
    #                                 "departure": {  
    #                                     "iataCode": "PTY",  
    #                                     "at": "2024-08-20T18:50:00"  
    #                                 },  
    #                                 "arrival": {  
    #                                     "iataCode": "AMS",  
    #                                     "at": "2024-08-21T12:10:00"  
    #                                 },  
    #                                 "carrierCode": "KL",  
    #                                 "number": "7891",  
    #                                 "aircraft": {  
    #                                     "code": "77W"  
    #                                 },  
    #                                 "operating": {  
    #                                     "carrierCode": "KL"  
    #                                 }  
    #                             },  
    #                             {  
    #                                 "departure": {  
    #                                     "iataCode": "AMS",  
    #                                     "at": "2024-08-21T14:05:00"  
    #                                 },  
    #                                 "arrival": {  
    #                                     "iataCode": "CDG",  
    #                                     "terminal": "2F",  
    #                                     "at": "2024-08-21T15:30:00"  
    #                                 },  
    #                                 "carrierCode": "KL",  
    #                                 "number": "1235",  
    #                                 "aircraft": {  
    #                                     "code": "738"  
    #                                 },  
    #                                 "operating": {  
    #                                     "carrierCode": "KL"  
    #                                 }  
    #                             }  
    #                         ]  
    #                     }  
    #                 ],  
    #                 "price": {  
    #                     "currency": "EUR",  
    #                     "total": "4740.32",  
    #                     "base": "4500.00",  
    #                     "fees": [  
    #                         {  
    #                             "amount": "240.32",  
    #                             "type": "TOTAL"  
    #                         }  
    #                     ]  
    #                 },  
    #                 "pricingOptions": {  
    #                     "fareType": [  
    #                         "PUBLISHED"  
    #                     ],  
    #                     "includedCheckedBagsOnly": True  
    #                 },  
    #                 "validatingAirlineCodes": [  
    #                     "KL"  
    #                 ],  
    #                 "travelerPricings": [  
    #                     {  
    #                         "travelerId": "1",  
    #                         "fareOption": "STANDARD",  
    #                         "travelerType": "ADULT",  
    #                         "price": {  
    #                             "currency": "EUR",  
    #                             "total": "1185.08",  
    #                             "base": "1125.00"  
    #                         },  
    #                         "fareDetailsBySegment": [  
    #                             {  
    #                                 "segmentId": "1",  
    #                                 "cabin": "ECONOMY",  
    #                                 "fareBasis": "ECO",  
    #                                 "class": "E"  
    #                             },  
    #                             {  
    #                                 "segmentId": "2",  
    #                                 "cabin": "ECONOMY",  
    #                                 "fareBasis": "ECO",  
    #                                 "class": "E"  
    #                             },  
    #                             {  
    #                                 "segmentId": "3",  
    #                                 "cabin": "ECONOMY",  
    #                                 "fareBasis": "ECO",  
    #                                 "class": "E"  
    #                             },  
    #                             {  
    #                                 "segmentId": "4",  
    #                                 "cabin": "ECONOMY",  
    #                                 "fareBasis": "ECO",  
    #                                 "class": "E"  
    #                             },  
    #                             {  
    #                                 "segmentId": "5",  
    #                                 "cabin": "ECONOMY",  
    #                                 "fareBasis": "ECO",  
    #                                 "class": "E"  
    #                             },  
    #                             {  
    #                                 "segmentId": "6",  
    #                                 "cabin": "ECONOMY",  
    #                                 "fareBasis": "ECO",  
    #                                 "class": "E"  
    #                             }  
    #                         ]  
    #                     },  
    #                     {  
    #                         "travelerId": "2",  
    #                         "fareOption": "STANDARD",  
    #                         "travelerType": "ADULT",  
    #                         "price": {  
    #                             "currency": "EUR",  
    #                             "total": "1185.08",  
    #                             "base": "1125.00"  
    #                         },  
    #                         "fareDetailsBySegment": [  
    #                             {  
    #                                 "segmentId": "1",  
    #                                 "cabin": "ECONOMY",  
    #                                 "fareBasis": "ECO",  
    #                                 "class": "E"  
    #                             },  
    #                             {  
    #                                 "segmentId": "2",  
    #                                 "cabin": "ECONOMY",  
    #                                 "fareBasis": "ECO",  
    #                                 "class": "E"  
    #                             },  
    #                             {  
    #                                 "segmentId": "3",  
    #                                 "cabin": "ECONOMY",  
    #                                 "fareBasis": "ECO",  
    #                                 "class": "E"  
    #                             },  
    #                             {  
    #                                 "segmentId": "4",  
    #                                 "cabin": "ECONOMY",  
    #                                 "fareBasis": "ECO",  
    #                                 "class": "E"  
    #                             },  
    #                             {  
    #                                 "segmentId": "5",  
    #                                 "cabin": "ECONOMY",  
    #                                 "fareBasis": "ECO",  
    #                                 "class": "E"  
    #                             },  
    #                             {  
    #                                 "segmentId": "6",  
    #                                 "cabin": "ECONOMY",  
    #                                 "fareBasis": "ECO",  
    #                                 "class": "E"  
    #                             }  
    #                         ]  
    #                     },  
    #                     {  
    #                         "travelerId": "3",  
    #                         "fareOption": "STANDARD",  
    #                         "travelerType": "CHILD",  
    #                         "price": {  
    #                             "currency": "EUR",  
    #                             "total": "1185.08",  
    #                             "base": "1125.00"  
    #                         },  
    #                         "fareDetailsBySegment": [  
    #                             {  
    #                                 "segmentId": "1",  
    #                                 "cabin": "ECONOMY",  
    #                                 "fareBasis": "ECO",  
    #                                 "class": "E"  
    #                             },  
    #                             {  
    #                                 "segmentId": "2",  
    #                                 "cabin": "ECONOMY",  
    #                                 "fareBasis": "ECO",  
    #                                 "class": "E"  
    #                             },  
    #                             {  
    #                                 "segmentId": "3",  
    #                                 "cabin": "ECONOMY",  
    #                                 "fareBasis": "ECO",  
    #                                 "class": "E"  
    #                             },  
    #                             {  
    #                                 "segmentId": "4",  
    #                                 "cabin": "ECONOMY",  
    #                                 "fareBasis": "ECO",  
    #                                 "class": "E"  
    #                             },  
    #                             {  
    #                                 "segmentId": "5",  
    #                                 "cabin": "ECONOMY",  
    #                                 "fareBasis": "ECO",  
    #                                 "class": "E"  
    #                             },  
    #                             {  
    #                                 "segmentId": "6",  
    #                                 "cabin": "ECONOMY",  
    #                                 "fareBasis": "ECO",  
    #                                 "class": "E"  
    #                             }  
    #                         ]  
    #                     },  
    #                     {  
    #                         "travelerId": "4",  
    #                         "fareOption": "STANDARD",  
    #                         "travelerType": "CHILD",  
    #                         "price": {  
    #                             "currency": "EUR",  
    #                             "total": "1185.08",  
    #                             "base": "1125.00"  
    #                         },  
    #                         "fareDetailsBySegment": [  
    #                             {  
    #                                 "segmentId": "1",  
    #                                 "cabin": "ECONOMY",  
    #                                 "fareBasis": "ECO",  
    #                                 "class": "E"  
    #                             },  
    #                             {  
    #                                 "segmentId": "2",  
    #                                 "cabin": "ECONOMY",  
    #                                 "fareBasis": "ECO",  
    #                                 "class": "E"  
    #                             },  
    #                             {  
    #                                 "segmentId": "3",  
    #                                 "cabin": "ECONOMY",  
    #                                 "fareBasis": "ECO",  
    #                                 "class": "E"  
    #                             },  
    #                             {  
    #                                 "segmentId": "4",  
    #                                 "cabin": "ECONOMY",  
    #                                 "fareBasis": "ECO",  
    #                                 "class": "E"  
    #                             },  
    #                             {  
    #                                 "segmentId": "5",  
    #                                 "cabin": "ECONOMY",  
    #                                 "fareBasis": "ECO",  
    #                                 "class": "E"  
    #                             },  
    #                             {  
    #                                 "segmentId": "6",  
    #                                 "cabin": "ECONOMY",  
    #                                 "fareBasis": "ECO",  
    #                                 "class": "E"  
    #                             }  
    #                         ]  
    #                     }  
    #                 ]  
    #             }  
    #         ]  
    #     }  
    # }  
    
    body = {
        "data": {
            "type": "flight-order",
            "flightOffers": [
                {
                    "type": "flight-offer",
                    "id": "1",
                    "source": "GDS",
                    "instantTicketingRequired": False,
                    "nonHomogeneous": False,
                    "paymentCardRequired": False,
                    "lastTicketingDate": "2020-03-01",
                    "itineraries": [
                        {
                            "segments": [
                                {
                                    "departure": {
                                        "iataCode": "GIG",
                                        "terminal": "2",
                                        "at": "2020-03-01T21:05:00",
                                    },
                                    "arrival": {
                                        "iataCode": "CDG",
                                        "terminal": "2E",
                                        "at": "2020-03-02T12:20:00",
                                    },
                                    "carrierCode": "KL",
                                    "number": "2410",
                                    "aircraft": {"code": "772"},
                                    "operating": {"carrierCode": "AF"},
                                    "duration": "PT11H15M",
                                    "id": "40",
                                    "numberOfStops": 0,
                                },
                                {
                                    "departure": {
                                        "iataCode": "CDG",
                                        "terminal": "2F",
                                        "at": "2020-03-02T14:30:00",
                                    },
                                    "arrival": {
                                        "iataCode": "AMS",
                                        "at": "2020-03-02T15:45:00",
                                    },
                                    "carrierCode": "KL",
                                    "number": "1234",
                                    "aircraft": {"code": "73H"},
                                    "operating": {"carrierCode": "KL"},
                                    "duration": "PT1H15M",
                                    "id": "41",
                                    "numberOfStops": 0,
                                },
                                {
                                    "departure": {
                                        "iataCode": "AMS",
                                        "at": "2020-03-02T17:05:00",
                                    },
                                    "arrival": {
                                        "iataCode": "MAD",
                                        "terminal": "2",
                                        "at": "2020-03-02T19:35:00",
                                    },
                                    "carrierCode": "KL",
                                    "number": "1705",
                                    "aircraft": {"code": "73J"},
                                    "operating": {"carrierCode": "KL"},
                                    "duration": "PT2H30M",
                                    "id": "42",
                                    "numberOfStops": 0,
                                },
                            ]
                        },
                        {
                            "segments": [
                                {
                                    "departure": {
                                        "iataCode": "MAD",
                                        "terminal": "2",
                                        "at": "2020-03-05T20:25:00",
                                    },
                                    "arrival": {
                                        "iataCode": "AMS",
                                        "at": "2020-03-05T23:00:00",
                                    },
                                    "carrierCode": "KL",
                                    "number": "1706",
                                    "aircraft": {"code": "73J"},
                                    "operating": {"carrierCode": "KL"},
                                    "duration": "PT2H35M",
                                    "id": "81",
                                    "numberOfStops": 0,
                                },
                                {
                                    "departure": {
                                        "iataCode": "AMS",
                                        "at": "2020-03-06T10:40:00",
                                    },
                                    "arrival": {
                                        "iataCode": "GIG",
                                        "terminal": "2",
                                        "at": "2020-03-06T18:35:00",
                                    },
                                    "carrierCode": "KL",
                                    "number": "705",
                                    "aircraft": {"code": "772"},
                                    "operating": {"carrierCode": "KL"},
                                    "duration": "PT11H55M",
                                    "id": "82",
                                    "numberOfStops": 0,
                                },
                            ]
                        },
                    ],
                    "price": {
                        "currency": "USD",
                        "total": "8514.96",
                        "base": "8314.00",
                        "fees": [
                            {"amount": "0.00", "type": "SUPPLIER"},
                            {"amount": "0.00", "type": "TICKETING"},
                            {"amount": "0.00", "type": "FORM_OF_PAYMENT"},
                        ],
                        "grandTotal": "8514.96",
                        "billingCurrency": "USD",
                    },
                    "pricingOptions": {
                        "fareType": ["PUBLISHED"],
                        "includedCheckedBagsOnly": True,
                    },
                    "validatingAirlineCodes": ["AF"],
                    "travelerPricings": [
                        {
                            "travelerId": "1",
                            "fareOption": "STANDARD",
                            "travelerType": "ADULT",
                            "price": {
                                "currency": "USD",
                                "total": "4849.48",
                                "base": "4749.00",
                                "taxes": [
                                    {"amount": "31.94", "code": "BR"},
                                    {"amount": "14.68", "code": "CJ"},
                                    {"amount": "5.28", "code": "FR"},
                                    {"amount": "17.38", "code": "JD"},
                                    {"amount": "0.69", "code": "OG"},
                                    {"amount": "3.95", "code": "QV"},
                                    {"amount": "12.12", "code": "QX"},
                                    {"amount": "14.44", "code": "RN"},
                                ],
                            },
                            "fareDetailsBySegment": [
                                {
                                    "segmentId": "40",
                                    "cabin": "BUSINESS",
                                    "fareBasis": "CFFBR",
                                    "brandedFare": "BUSINESS",
                                    "class": "C",
                                    "includedCheckedBags": {"quantity": 2},
                                },
                                {
                                    "segmentId": "41",
                                    "cabin": "BUSINESS",
                                    "fareBasis": "CFFBR",
                                    "brandedFare": "BUSINESS",
                                    "class": "J",
                                    "includedCheckedBags": {"quantity": 2},
                                },
                                {
                                    "segmentId": "42",
                                    "cabin": "BUSINESS",
                                    "fareBasis": "CFFBR",
                                    "brandedFare": "BUSINESS",
                                    "class": "J",
                                    "includedCheckedBags": {"quantity": 2},
                                },
                                {
                                    "segmentId": "81",
                                    "cabin": "ECONOMY",
                                    "fareBasis": "YFFBR",
                                    "brandedFare": "FULLFLEX",
                                    "class": "Y",
                                    "includedCheckedBags": {"quantity": 1},
                                },
                                {
                                    "segmentId": "82",
                                    "cabin": "ECONOMY",
                                    "fareBasis": "YFFBR",
                                    "brandedFare": "FULLFLEX",
                                    "class": "Y",
                                    "includedCheckedBags": {"quantity": 1},
                                },
                            ],
                        },
                        {
                            "travelerId": "2",
                            "fareOption": "STANDARD",
                            "travelerType": "CHILD",
                            "price": {
                                "currency": "USD",
                                "total": "3665.48",
                                "base": "3565.00",
                                "taxes": [
                                    {"amount": "31.94", "code": "BR"},
                                    {"amount": "14.68", "code": "CJ"},
                                    {"amount": "5.28", "code": "FR"},
                                    {"amount": "17.38", "code": "JD"},
                                    {"amount": "0.69", "code": "OG"},
                                    {"amount": "3.95", "code": "QV"},
                                    {"amount": "12.12", "code": "QX"},
                                    {"amount": "14.44", "code": "RN"},
                                ],
                            },
                            "fareDetailsBySegment": [
                                {
                                    "segmentId": "40",
                                    "cabin": "BUSINESS",
                                    "fareBasis": "CFFBR",
                                    "brandedFare": "BUSINESS",
                                    "class": "C",
                                    "includedCheckedBags": {"quantity": 2},
                                },
                                {
                                    "segmentId": "41",
                                    "cabin": "BUSINESS",
                                    "fareBasis": "CFFBR",
                                    "brandedFare": "BUSINESS",
                                    "class": "J",
                                    "includedCheckedBags": {"quantity": 2},
                                },
                                {
                                    "segmentId": "42",
                                    "cabin": "BUSINESS",
                                    "fareBasis": "CFFBR",
                                    "brandedFare": "BUSINESS",
                                    "class": "J",
                                    "includedCheckedBags": {"quantity": 2},
                                },
                                {
                                    "segmentId": "81",
                                    "cabin": "ECONOMY",
                                    "fareBasis": "YFFBR",
                                    "brandedFare": "FULLFLEX",
                                    "class": "Y",
                                    "includedCheckedBags": {"quantity": 1},
                                },
                                {
                                    "segmentId": "82",
                                    "cabin": "ECONOMY",
                                    "fareBasis": "YFFBR",
                                    "brandedFare": "FULLFLEX",
                                    "class": "Y",
                                    "includedCheckedBags": {"quantity": 1},
                                },
                            ],
                        },
                    ],
                }
            ],
            "travelers": [
                {
                    "id": "1",
                    "dateOfBirth": "1982-01-16",
                    "name": {"firstName": "JORGE", "lastName": "GONZALES"},
                    "gender": "MALE",
                    "contact": {
                        "emailAddress": "jorge.gonzales833@telefonica.es",
                        "phones": [
                            {
                                "deviceType": "MOBILE",
                                "countryCallingCode": "34",
                                "number": "480080076",
                            }
                        ],
                    },
                    "documents": [
                        {
                            "documentType": "PASSPORT",
                            "birthPlace": "Madrid",
                            "issuanceLocation": "Madrid",
                            "issuanceDate": "2015-04-14",
                            "number": "00000000",
                            "expiryDate": "2025-04-14",
                            "issuanceCountry": "ES",
                            "validityCountry": "ES",
                            "nationality": "ES",
                            "holder": True,
                        }
                    ],
                },
                {
                    "id": "2",
                    "dateOfBirth": "2012-10-11",
                    "gender": "FEMALE",
                    "contact": {
                        "emailAddress": "jorge.gonzales833@telefonica.es",
                        "phones": [
                            {
                                "deviceType": "MOBILE",
                                "countryCallingCode": "34",
                                "number": "480080076",
                            }
                        ],
                    },
                    "name": {"firstName": "ADRIANA", "lastName": "GONZALES"},
                },
            ],
            "remarks": {
                "general": [
                    {
                        "subType": "GENERAL_MISCELLANEOUS",
                        "text": "ONLINE BOOKING FROM INCREIBLE VIAJES",
                    }
                ]
            },
            "ticketingAgreement": {"option": "DELAY_TO_CANCEL", "delay": "6D"},
            "contacts": [
                {
                    "addresseeName": {"firstName": "PABLO", "lastName": "RODRIGUEZ"},
                    "companyName": "INCREIBLE VIAJES",
                    "purpose": "STANDARD",
                    "phones": [
                        {
                            "deviceType": "LANDLINE",
                            "countryCallingCode": "34",
                            "number": "480080071",
                        },
                        {
                            "deviceType": "MOBILE",
                            "countryCallingCode": "33",
                            "number": "480080072",
                        },
                    ],
                    "emailAddress": "support@increibleviajes.es",
                    "address": {
                        "lines": ["Calle Prado, 16"],
                        "postalCode": "28014",
                        "cityName": "Madrid",
                        "countryCode": "ES",
                    },
                }
            ],
        }
    }

    
    response = await api_wrapper.request(endpoint, method, body=body)  
    print(response)  

# Execute the main function  
asyncio.run(main())  