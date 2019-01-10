# GenerateWeather.py
# Your Name
# Date

"""
    Place an informative doc string here in the required style.
"""

import Weather

def WindChill(T,W):
    """
    Place an informative doc string here in the required style.
    """
    # Develop the function body here...
       
    return float(T)

def Test(T,W,TrueWC):
    """  Prints T, W, WindChill(T,W) and the True Windchill
    
    Precondition: T is a  valid temperature string, W is a valid wind string, and TrueWC is
    the actual wind chill asociated with T and W.
    """
    
    WC = WindChill(T,W)
    print 'WindChill returns %4d     Actual = %5.1f    Input = (%s,%s)    ' % (WindChill(T,W),TrueWC,T,W)

#Application Script 
if __name__ == '__main__':
    """ Confirms the correctness of WindChill in
    ten different representative cases."""

    Test('85','100kph',85)
     
     
     

    

    
   
    






