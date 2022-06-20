import socket
import geocoder
import folium
import webbrowser
# Function to display hostname and
# IP address
def get_Host_name_IP():
    try:
        host_name = socket.gethostname()
        host_ip = socket.gethostbyname(host_name)
        print("Hostname :  ",host_name)
        print("IP : ",host_ip)
        g=geocoder.ip("me")
        myaddress=g.latlng
        my_map1=folium.Map(location=myaddress,zoom_start=10)

        folium.CircleMarker(location=myaddress,radius=50,popup="Bharuch",color="red").add_to(my_map1)
        folium.Marker(myaddress,popup="Bharuch").add_to(my_map1)
        my_map1.save("mymap.html")
        webbrowser.open_new_tab('mymap.html')
        
    except:
        print("Unable to get Hostname and IP")     
        
get_Host_name_IP()