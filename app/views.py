from django.shortcuts import render,redirect,HttpResponse
from . forms import ProfileForm,ExtendedForm,ExtendedUpdateForm,ProfileUpdateForm,ConsentDocumentForm
from django.contrib.auth.models import User
from . models import ConsentDocument,ConsentStatus,Profile,corban_pricing,economic_forecast,co2_emission,energy_cost
from django.contrib import messages
import datetime
from django.utils import timezone
import random
import pandas as pd
from django.http import JsonResponse
from django.db.models import Q

def random_color():
    return "#{:06x}".format(random.randint(0, 0xFFFFFF))

def location_data(data_from):
    countries_data = [["AGO", -11.2027, 17.8739],["ALB", 41.1533, 20.1683],["ARE", 23.4241, 53.8478],["ARG", -38.4161, -63.6167],["ARM", 40.0691, 45.0382],["AUS", -25.2744, 133.7751],["AUT", 47.5162, 14.5501],["AZE", 40.1431, 47.5769],["BEL", 50.5039, 4.4699],["BEN", 9.3077, 2.3158],["BGD", 23.6850, 90.3563],["BGR", 42.7339, 25.4858],["BHR", 25.9304, 50.6378],["BIH", 43.9159, 17.6791],["BLR", 53.7098, 27.9534],["BOL", -16.2902, -63.5887],["BRA", -14.2350, -51.9253],["BRN", 4.5353, 114.7277],["BWA", -22.3285, 24.6849],
    ["CAN", 56.1304, -106.3468],
    ["CHE", 46.8182, 8.2275],
    ["CHL", -35.6751, -71.5430],
    ["CHN", 35.8617, 104.1954],
    ["CIV", 7.539989, -5.5471],
    ["CMR", 7.3697, 12.3547],
    ["COD", -4.0383, 21.7587],
    ["COG", -0.2280, 15.8277],
    ["COL", 4.5709, -74.2973],
    ["CRI", 9.7489, -83.7534],
    ["CUB", 21.5218, -77.7812],
    ["CYP", 35.1264, 33.4299],
    ["CZE", 49.8175, 15.4730],
    ["DEU", 51.1657, 10.4515],
    ["DNK", 56.2639, 9.5018],
    ["DOM", 18.7357, -70.1627],
    ["DZA", 28.0339, 1.6596],
    ["ECU", -1.8312, -78.1834],
    ["EGY", 26.8206, 30.8025],
    ["ERI", 15.1794, 39.7823],
    ["ESP", 40.4637, -3.7492],
    ["EST", 58.5953, 25.0136],
    ["ETH", 9.1450, 40.4897],
    ["EU27", 53.1424, 7.6921],
    ["FIN", 61.9241, 25.7482],
    ["FRA", 46.6034, 1.8883],
    ["GAB", -0.8037, 11.6094],
    ["GBR", 55.3781, -3.4360],
    ["GEO", 42.3154, 43.3569],
    ["GHA", 7.9465, -1.0232],
    ["GRC", 39.0742, 21.8243],
    ["GTM", 15.7835, -90.2308],
    ["HKG", 22.3193, 114.1694],
    ["HND", 15.2000, -86.2419],
    ["HRV", 45.1000, 15.2000],
    ["HTI", 18.9712, -72.2852],
    ["HUN", 47.1625, 19.5033],
    ["IDN", -0.7893, 113.9213],
    ["IND", 20.5937, 78.9629],
    ["IRL", 53.1424, -7.6921],
    ["IRN", 32.4279, 53.6880],
    ["IRQ", 33.2232, 43.6793],
    ["ISL", 64.9631, -19.0208],
    ["ISR", 31.0461, 34.8516],
    ["ITA", 41.8719, 12.5674],
    ["JAM", 18.1096, -77.2975],
    ["JOR", 30.5852, 36.2384],
    ["JPN", 36.2048, 138.2529],
    ["KAZ", 48.0196, 66.9237],
    ["KEN", -1.286389, 36.817223],
    ["KGZ", 41.2044, 74.7661],
    ["KHM", 12.5657, 104.9910],
    ["KOR", 35.9078, 127.7669],
    ["KWT", 29.3117, 47.4818],
    ["LBN", 33.8547, 35.8623],
    ["LBY", 26.3351, 17.2283],
    ["LKA", 7.8731, 80.7718],
    ["LTU", 55.1694, 23.8813],
    ["LUX", 49.8153, 6.1296],
    ["LVA", 56.8796, 24.6032],
    ["MAR", 31.7917, -7.0926],
    ["MDA", 47.4116, 28.3699],
    ["MEX", 23.6345, -102.5528],
    ["MKD", 41.6086, 21.7453],
    ["MLI", 17.5707, -3.9962],
    ["MLT", 35.8997, 14.5146],
    ["MMR", 21.9162, 95.9560],
    ["MNE", 42.7087, 19.3744],
    ["MNG", 46.8625, 103.8467],
    ["MOZ", -18.6657, 35.5296],
    ["MUS", -20.3484, 57.5522],
    ["MYS", 4.2105, 101.9758],
    ["NAM", -22.9576, 18.4904],
    ["NER", 17.6078, 8.0817],
    ["NGA", 9.0820, 8.6753],
    ["NIC", 12.8654, -85.2072],
    ["NLD", 52.1326, 5.2913],
    ["NOR", 60.4720, 8.4689],
    ["NPL", 28.3949, 84.1240],
    ["NZL", -40.9006, 174.8860],
    ["OMN", 21.4735, 55.9754],
    ["PAK", 30.3753, 69.3451],
    ["PAN", 8.5380, -80.7821],
    ["PER", -9.189967, -75.0152],
    ["PHL", 12.8797, 121.7740],
    ["POL", 51.9194, 19.1451],
    ["PRK", 40.3399, 127.5101],
    ["PRT", 39.3999, -8.2245],
    ["PRY", -23.4425, -58.4438],
    ["QAT", 25.3548, 51.1839],
    ["ROU", 45.9432, 24.9668],
    ["RUS", 61.5240, 105.3188],
    ["SAU", 23.8859, 45.0792],
    ["SDN", 12.8628, 30.2176],
    ["SEN", 14.4974, -14.4524],
    ["SGP", 1.3521, 103.8198],
    ["SLV", 13.7942, -88.8965],
    ["SRB", 44.0165, 21.0059],
    ["SSD", 7.8627, 29.6949],
    ["SUR", 3.9193, -56.0278],
    ["SVK", 48.6690, 19.6990],
    ["SVN", 46.1512, 14.9955],
    ["SWE", 60.1282, 18.6435],
    ["SYR", 34.8021, 38.9968],
    ["TGO", 8.6195, 0.8248],
    ["THA", 15.8700, 100.9925],
    ["TJK", 38.8610, 71.2761],
    ["TKM", 38.9697, 59.5563],
    ["TTO", 10.6918, -61.2225],
    ["TUN", 33.8869, 9.5375],
    ["TUR", 38.9637, 35.2433],
    ["TWN", 23.6978, 120.9605],
    ["TZA", -6.3690, 34.8888],
    ["UGA", 1.3733, 32.2903],
    ["UKR", 48.3794, 31.1656],
    ["URY", -32.5228, -55.7658],
    ["USA", 37.0902, -95.7129],
    ["UZB", 41.3775, 64.5853],
    ["VEN", 6.4238, -66.5897],
    ["VNM", 14.0583, 108.2772],
    ["YEM", 15.5527, 48.5164],
    ["ZAF", -30.5595, 22.9375],
    ["ZMB", -13.1339, 27.8493],
    ["ZWE", -19.0154, 29.1549],
    ]
    df = pd.DataFrame(countries_data, columns=["Country_Code", "Latitude", "Longitude"])
    if data_from=="economic":
        corban_pricing_data=pd.DataFrame(list(economic_forecast.objects.all().values()))
    elif data_from=="co2":
        corban_pricing_data=pd.DataFrame(list(co2_emission.objects.all().values()))
    elif data_from=="energy":
        corban_pricing_data=pd.DataFrame(list(energy_cost.objects.all().values()))
    else:
        corban_pricing_data=pd.DataFrame(list(corban_pricing.objects.all().values()))
    df=pd.merge(corban_pricing_data,df,how="inner",left_on="region",right_on="Country_Code")
    return df
# Create your views here.
def home(request):
    if request.user.is_authenticated:
        return redirect('log')
    else:
        return render(request,'home.html')

def register(request):
    if request.user.is_authenticated:
        return redirect('log')
    else:
        if request.method =='POST':
            email = request.POST['email']
            form = ExtendedForm(request.POST)
            user_profile = ProfileForm(request.POST,request.FILES)
            if form.is_valid() and user_profile.is_valid():
                try:
                    user = form.save()
                    profile = user_profile.save(commit=False)
                    profile.user = user
                    profile.save()
                    return redirect('/')
                except:
                    messages.info(request,'invalid mail')
                    return redirect('signup')
            else:
                messages.info(request,'invalid details')
                return redirect('signup')
        else:
            form = ExtendedForm()
            user_profile = ProfileForm()
            return render(request,'register.html',{'form':form,'form1':user_profile})
    
def log(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            scenarios=corban_pricing.objects.values("scenario").distinct()
            region=corban_pricing.objects.values("region").distinct()
            region_category = corban_pricing.objects.values("region_category").distinct()
            region_category_temp_list = corban_pricing.objects.values_list("region_category").distinct()
            scenario_name = request.POST.getlist('scenario',['Below 2?C','Current Policies','Delayed transition', 'Fragmented World', 'Low demand',  'Nationally Determined Contributions (NDCs)',  'Net Zero 2050'])
            region_name =  request.POST.getlist('region',["World"])
            year_first = request.POST.getlist("year_first",['2020','2025','2030','2035'])
            region_category_temp=[i[0] for i in region_category_temp_list]
            region_category_list=[]
            region_name_list=[]
            for i in region_name:
                if i in region_category_temp:
                    region_category_list.append(i)
                else:
                    region_name_list.append(i)
            if region_category_list:
                corban_pricing_datasets=corban_pricing.objects.filter(scenario__in=scenario_name).filter(region_category__in=region_category_list)
                corban_pricing_data=corban_pricing.objects.filter(scenario__in=scenario_name).filter(region_category__in=region_category_list).values_list(*[field.name for field in corban_pricing._meta.get_fields() if field.name.startswith('year') and field.name[len(field.name)-4:] in year_first])
            else:
                corban_pricing_datasets=corban_pricing.objects.filter(scenario__in=scenario_name).filter(region__in=region_name_list)
                corban_pricing_data=corban_pricing.objects.filter(scenario__in=scenario_name).filter(region__in=region_name_list).values_list(*[field.name for field in corban_pricing._meta.get_fields() if field.name.startswith('year') and field.name[len(field.name)-4:] in year_first])
            labels =[field.name[5:] for field in corban_pricing._meta.get_fields() if field.name.startswith('year')]
            labels_chart =[i for i in [field.name[5:] for field in corban_pricing._meta.get_fields() if field.name.startswith('year')] if i in year_first]
            
            datasets = []
            for i,j in zip(corban_pricing_datasets,corban_pricing_data):
                datasets.append({"label": i.region+" "+i.scenario,"data":list(j),"borderColor": random_color()})

            #map
            queryset_main = location_data("carbon")
            scenario_map = request.POST.get('scenario_map', "Net Zero 2050")
            year_map = "year_"+request.POST.get('year_map', '2100')
            queryset=queryset_main[queryset_main["scenario"]==scenario_map]
            geojson_data = {
                "type": "FeatureCollection",
                "features": []
            }

            for _, record in queryset.iterrows():  # Use iterrows to iterate through DataFrame rows
                feature = {
                    "type": "Feature",
                    "geometry": {
                    "type": "Point",
                    "coordinates": [record["Longitude"], record["Latitude"]],
                    },
                    "properties": {
                    "region": record["region"],         # Access fields using column names
                    "scenario": record["scenario"],
                    "year_label":year_map[5:],
                    "price_2100": record[year_map],
                    }
                }
                geojson_data["features"].append(feature)
                
            #top Bottom
            topbottom = request.POST.get('topbottom', "top")
            topbottomn = request.POST.get('topbottomn', '5')
            numeric_data = queryset_main.select_dtypes(include=['number'])
            queryset_main["mean"]=numeric_data.mean(axis=1)
            queryset_main = queryset_main.sort_values(by='mean', ascending=False)
            topbottom_datasets = []
            if topbottom=="top":
                queryset_main=queryset_main.head(int(topbottomn))
            else:
                queryset_main=queryset_main.tail(int(topbottomn))
            for _, record in queryset_main.iterrows():
                topbottom_datasets.append({"label": record["region"]+" "+record["scenario"],"data":record.filter(regex='^year_').values.tolist(),"borderColor": random_color()})

            #table
            corban_pricing_data_table=pd.DataFrame(list(corban_pricing.objects.all().values()))
            scenario_table = request.POST.getlist('scenario_table', ["Low demand"])
            region_table = request.POST.getlist('region_table', ["World"])
            year_table = request.POST.getlist('year_table', ['2025'])
            corban_pricing_data_table1=corban_pricing_data_table[(corban_pricing_data_table["scenario"].isin(scenario_table)) & (corban_pricing_data_table["region"].isin(region_table))]
            corban_pricing_data_table2=corban_pricing_data_table[(corban_pricing_data_table["scenario"].isin(scenario_table)) & (corban_pricing_data_table["region_category"].isin(region_table))]
            corban_pricing_data_table = pd.concat([corban_pricing_data_table1, corban_pricing_data_table2], ignore_index=True)
            corban_pricing_data_table=corban_pricing_data_table[["scenario","region_category","region","unit"]+["year_"+i for i in year_table]]
            corban_pricing_data_table_year=corban_pricing_data_table[[col for col in corban_pricing_data_table.columns if col.startswith('year')]].values.tolist()
            corban_pricing_data_table_main=[]
            for i in range(len(corban_pricing_data_table)):
                corban_pricing_data_table_main.append({"srno":i+1,"scenario":corban_pricing_data_table["scenario"][i],"region_category":corban_pricing_data_table["region_category"][i],"region":corban_pricing_data_table["region"][i],"unit":corban_pricing_data_table["unit"][i],"year":corban_pricing_data_table_year[i]})
            
            #export
            if "export" in request.POST:
                response = HttpResponse(content_type='text/csv')
                response['Content-Disposition'] = 'attachment; filename="data.csv"'
                corban_pricing_data_table.to_csv(path_or_buf=response, index=False)
                return response
            
            #Comparison
            form_option = request.POST.get('option', "")
            scenario_form = request.POST.get('scenario_form', "")
            scenario_form2 = request.POST.get('scenario_form2', "")
            region_form = request.POST.get('region_form', "")
            region_form2 = request.POST.get('region_form2', "")
            year_form = request.POST.get('year_form', "")
            year_form2 = request.POST.get('year_form2', "")
            comparison_datasets = []
            comparison_labels = []
            if form_option=="1":
                year="year_"+year_form
                corban_pricing_form_data=corban_pricing.objects.filter(Q(region=region_form) | Q(region=region_form2)).filter(Q(scenario=scenario_form))
                for i in corban_pricing_form_data:
                    comparison_labels.append( i.region+" "+i.scenario+" "+year_form)
                    comparison_datasets.append(getattr(i, year, None))
            elif form_option=="2":
                year="year_"+year_form
                corban_pricing_form_data=corban_pricing.objects.filter(Q(scenario=scenario_form)| Q(scenario=scenario_form2)).filter(Q(region=region_form))
                for i in corban_pricing_form_data:
                    comparison_labels.append( i.region+" "+i.scenario+" "+year_form)
                    comparison_datasets.append(getattr(i, year, None))
            else:
                year="year_"+year_form
                year2="year_"+year_form2
                corban_pricing_form_data=corban_pricing.objects.filter(Q(region=region_form) & Q(scenario=scenario_form))
                for i in corban_pricing_form_data:
                    comparison_labels.append( i.region+" "+i.scenario+" "+year_form)
                    comparison_datasets.append(getattr(i, year, None))
                    comparison_labels.append( i.region+" "+i.scenario+" "+year_form2)
                    comparison_datasets.append(getattr(i, year2, None))

            return render(request,'profile.html',{"scenarios":scenarios,"region":region,"year_first":year_first,"scenario_name":scenario_name,"region_name":region_name,"region_category":region_category,"datasets":datasets,"labels":labels,"labels_chart":labels_chart,"geojson_data":geojson_data,"scenario_map":scenario_map,"year_map":year_map[5:],"topbottom":topbottom,"topbottomn":topbottomn,"topbottom_datasets":topbottom_datasets,"corban_pricing_data_table":corban_pricing_data_table_main,"scenario_table":scenario_table,"region_table":region_table,"year_table":year_table,"comparison_datasets":comparison_datasets,"comparison_labels":comparison_labels,"form_option":form_option,"scenario_form":scenario_form,"scenario_form2":scenario_form2,"region_form":region_form,"region_form2":region_form2,"year_form":year_form,"year_form2":year_form2})
        else:
            scenarios=corban_pricing.objects.values("scenario").distinct()
            region=corban_pricing.objects.values("region").distinct()
            region_category = corban_pricing.objects.values("region_category").distinct()
            region_category_temp_list = corban_pricing.objects.values_list("region_category").distinct()
            scenario_name = request.POST.getlist('scenario',['Below 2?C','Current Policies','Delayed transition', 'Fragmented World', 'Low demand',  'Nationally Determined Contributions (NDCs)',  'Net Zero 2050'])
            region_name =  request.POST.getlist('region',["World"])
            year_first = request.POST.getlist("year_first",['2020','2025','2030','2035'])
            region_category_temp=[i[0] for i in region_category_temp_list]
            region_category_list=[]
            region_name_list=[]
            for i in region_name:
                if i in region_category_temp:
                    region_category_list.append(i)
                else:
                    region_name_list.append(i)
            if region_category_list:
                corban_pricing_datasets=corban_pricing.objects.filter(scenario__in=scenario_name).filter(region_category__in=region_category_list)
                corban_pricing_data=corban_pricing.objects.filter(scenario__in=scenario_name).filter(region_category__in=region_category_list).values_list(*[field.name for field in corban_pricing._meta.get_fields() if field.name.startswith('year') and field.name[len(field.name)-4:] in year_first])
            else:
                corban_pricing_datasets=corban_pricing.objects.filter(scenario__in=scenario_name).filter(region__in=region_name_list)
                corban_pricing_data=corban_pricing.objects.filter(scenario__in=scenario_name).filter(region__in=region_name_list).values_list(*[field.name for field in corban_pricing._meta.get_fields() if field.name.startswith('year') and field.name[len(field.name)-4:] in year_first])
            labels =[field.name[5:] for field in corban_pricing._meta.get_fields() if field.name.startswith('year')]
            labels_chart =[i for i in [field.name[5:] for field in corban_pricing._meta.get_fields() if field.name.startswith('year')] if i in year_first]
            
            datasets=[]
            for i,j in zip(corban_pricing_datasets,corban_pricing_data):
                datasets.append({"label": i.region+" "+i.scenario,"data":list(j),"borderColor": random_color()})
            
            #map
            queryset_main = location_data("carbon")
            scenario_map = request.POST.get('scenario_map', "Net Zero 2050")
            year_map = "year_"+request.POST.get('year_map', '2100')
            geojson_data = {
                "type": "FeatureCollection",
                "features": []
            }
            queryset=queryset_main[(queryset_main["scenario"]==scenario_map)]

            for _, record in queryset.iterrows():  # Use iterrows to iterate through DataFrame rows
                feature = {
                    "type": "Feature",
                    "geometry": {
                    "type": "Point",
                    "coordinates": [record["Longitude"], record["Latitude"]],
                    },
                    "properties": {
                    "region": record["region"],         # Access fields using column names
                    "scenario": record["scenario"],
                    "year_label":year_map[5:],
                    "price_2100": record[year_map],
                    }
                }
                geojson_data["features"].append(feature)


            #top Bottom
            topbottom = request.POST.get('topbottom', "top")
            topbottomn = request.POST.get('topbottomn', '5')
            numeric_data = queryset_main.select_dtypes(include=['number'])
            queryset_main["mean"]=numeric_data.mean(axis=1)
            queryset_main = queryset_main.sort_values(by='mean', ascending=False)
            topbottom_datasets = []
            if topbottom=="top":
                queryset_main=queryset_main.head(int(topbottomn))
            else:
                queryset_main=queryset_main.tail(int(topbottomn))
            for _, record in queryset_main.iterrows():
                topbottom_datasets.append({"label": record["region"]+" "+record["scenario"],"data":record.filter(regex='^year_').values.tolist(),"borderColor": random_color()})

            #table
            corban_pricing_data_table=pd.DataFrame(list(corban_pricing.objects.all().values()))
            scenario_table = request.POST.getlist('scenario_table', ["Low demand"])
            region_table = request.POST.getlist('region_table', ["World"])
            year_table = request.POST.getlist('year_table', ['2025'])
            corban_pricing_data_table1=corban_pricing_data_table[(corban_pricing_data_table["scenario"].isin(scenario_table)) & (corban_pricing_data_table["region"].isin(region_table))]
            corban_pricing_data_table2=corban_pricing_data_table[(corban_pricing_data_table["scenario"].isin(scenario_table)) & (corban_pricing_data_table["region_category"].isin(region_table))]
            corban_pricing_data_table = pd.concat([corban_pricing_data_table1, corban_pricing_data_table2], ignore_index=True)
            corban_pricing_data_table=corban_pricing_data_table[["scenario","region_category","region","unit"]+["year_"+i for i in year_table]]
            corban_pricing_data_table_year=corban_pricing_data_table[[col for col in corban_pricing_data_table.columns if col.startswith('year')]].values.tolist()
            corban_pricing_data_table_main=[]
            for i in range(len(corban_pricing_data_table)):
                corban_pricing_data_table_main.append({"srno":i+1,"scenario":corban_pricing_data_table["scenario"][i],"region_category":corban_pricing_data_table["region_category"][i],"region":corban_pricing_data_table["region"][i],"unit":corban_pricing_data_table["unit"][i],"year":corban_pricing_data_table_year[i]})
            
            return render(request,'profile.html',{"scenarios":scenarios,"region":region,"year_first":year_first,"scenario_name":scenario_name,"region_name":region_name,"region_category":region_category,"datasets":datasets,"labels":labels,"labels_chart":labels_chart,"geojson_data":geojson_data,"scenario_map":scenario_map,"year_map":year_map[5:],"topbottom":topbottom,"topbottomn":topbottomn,"topbottom_datasets":topbottom_datasets,"corban_pricing_data_table":corban_pricing_data_table_main,"scenario_table":scenario_table,"region_table":region_table,"year_table":year_table})
    else:
        return redirect('/')


def energy_cost1(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            scenarios=energy_cost.objects.values("scenario").distinct()
            region=energy_cost.objects.values("region").distinct()
            variable = energy_cost.objects.values("variable").distinct()
            region_category = energy_cost.objects.values("region_category").distinct()
            region_category_temp_list = energy_cost.objects.values_list("region_category").distinct()
            scenario_name = request.POST.getlist('scenario',['Below 2?C','Current Policies','Delayed transition', 'Fragmented World', 'Low demand',  'Nationally Determined Contributions (NDCs)',  'Net Zero 2050'])
            region_name =  request.POST.getlist('region',["World"])
            year_first = request.POST.getlist("year_first",['2020','2025','2030','2035'])
            variable_name = request.POST.getlist("variable",['Capital Cost|Electricity|Nuclear', 'Capital Cost|Electricity|Solar|CSP', 'Capital Cost|Electricity|Coal|w/o CCS', 'Capital Cost|Electricity|Gas|w/o CCS', 'Capital Cost|Electricity|Gas|w/ CCS', 'Capital Cost|Electricity|Geothermal', 'Capital Cost|Electricity|Biomass|w/o CCS', 'Capital Cost|Electricity|Wind|Onshore', 'Capital Cost|Electricity|Biomass|w/ CCS', 'Capital Cost|Electricity|Solar|PV', 'Capital Cost|Electricity|Coal|w/ CCS', 'Capital Cost|Electricity|Wind|Offshore'])
            region_category_temp=[i[0] for i in region_category_temp_list]
            region_category_list=[]
            region_name_list=[]
            for i in region_name:
                if i in region_category_temp:
                    region_category_list.append(i)
                else:
                    region_name_list.append(i)
            if region_category_list:
                energy_cost_datasets=energy_cost.objects.filter(scenario__in=scenario_name).filter(region_category__in=region_category_list).filter(variable__in=variable_name)
                energy_cost_data=energy_cost.objects.filter(scenario__in=scenario_name).filter(region_category__in=region_category_list).filter(variable__in=variable_name).values_list(*[field.name for field in energy_cost._meta.get_fields() if field.name.startswith('year') and field.name[len(field.name)-4:] in year_first])
            else:
                energy_cost_datasets=energy_cost.objects.filter(scenario__in=scenario_name).filter(region__in=region_name_list).filter(variable__in=variable_name)
                energy_cost_data=energy_cost.objects.filter(scenario__in=scenario_name).filter(region__in=region_name_list).filter(variable__in=variable_name).values_list(*[field.name for field in energy_cost._meta.get_fields() if field.name.startswith('year') and field.name[len(field.name)-4:] in year_first])
            labels =[field.name[5:] for field in energy_cost._meta.get_fields() if field.name.startswith('year')]
            labels_chart =[i for i in [field.name[5:] for field in energy_cost._meta.get_fields() if field.name.startswith('year')] if i in year_first]
            
            datasets = []
            for i,j in zip(energy_cost_datasets,energy_cost_data):
                datasets.append({"label": i.region+" "+i.scenario+" "+i.variable,"data":list(j),"borderColor": random_color()})

            #map
            queryset_main = location_data("energy")
            scenario_map = request.POST.get('scenario_map', "Net Zero 2050")
            year_map = "year_"+request.POST.get('year_map', '2100')
            queryset=queryset_main[queryset_main["scenario"]==scenario_map]
            geojson_data = {
                "type": "FeatureCollection",
                "features": []
            }

            for _, record in queryset.iterrows():  # Use iterrows to iterate through DataFrame rows
                feature = {
                    "type": "Feature",
                    "geometry": {
                    "type": "Point",
                    "coordinates": [record["Longitude"], record["Latitude"]],
                    },
                    "properties": {
                    "region": record["region"],         # Access fields using column names
                    "scenario": record["scenario"],
                    "year_label":year_map[5:],
                    "price_2100": record[year_map],
                    }
                }
                geojson_data["features"].append(feature)
                
            #top Bottom
            topbottom = request.POST.get('topbottom', "top")
            topbottomn = request.POST.get('topbottomn', '5')
            numeric_data = queryset_main.select_dtypes(include=['number'])
            queryset_main["mean"]=numeric_data.mean(axis=1)
            queryset_main = queryset_main.sort_values(by='mean', ascending=False)
            topbottom_datasets = []
            if topbottom=="top":
                queryset_main=queryset_main.head(int(topbottomn))
            else:
                queryset_main=queryset_main.tail(int(topbottomn))
            for _, record in queryset_main.iterrows():
                topbottom_datasets.append({"label": record["region"]+" "+record["scenario"],"data":record.filter(regex='^year_').values.tolist(),"borderColor": random_color()})
            print(topbottom_datasets)
            #table
            energy_cost_data_table=pd.DataFrame(list(energy_cost.objects.all().values()))
            scenario_table = request.POST.getlist('scenario_table', ["Low demand"])
            region_table = request.POST.getlist('region_table', ["World"])
            year_table = request.POST.getlist('year_table', ['2025'])
            variable_table = request.POST.getlist('variable_table')
            energy_cost_data_table1=energy_cost_data_table[(energy_cost_data_table["scenario"].isin(scenario_table)) & (energy_cost_data_table["region"].isin(region_table)) & (energy_cost_data_table["variable"].isin(variable_table))]
            energy_cost_data_table2=energy_cost_data_table[(energy_cost_data_table["scenario"].isin(scenario_table)) & (energy_cost_data_table["region_category"].isin(region_table)) & (energy_cost_data_table["variable"].isin(variable_table))]
            energy_cost_data_table = pd.concat([energy_cost_data_table1, energy_cost_data_table2], ignore_index=True)
            energy_cost_data_table=energy_cost_data_table[["scenario","region_category","region","unit","variable"]+["year_"+i for i in year_table]]
            energy_cost_data_table_year=energy_cost_data_table[[col for col in energy_cost_data_table.columns if col.startswith('year')]].values.tolist()
            energy_cost_data_table_main=[]
            for i in range(len(energy_cost_data_table)):
                energy_cost_data_table_main.append({"srno":i+1,"scenario":energy_cost_data_table["scenario"][i],"region_category":energy_cost_data_table["region_category"][i],"region":energy_cost_data_table["region"][i],"unit":energy_cost_data_table["unit"][i],"variable":energy_cost_data_table["variable"][i],"year":energy_cost_data_table_year[i]})
            #export
            if "export" in request.POST:
                response = HttpResponse(content_type='text/csv')
                response['Content-Disposition'] = 'attachment; filename="data.csv"'
                energy_cost_data_table.to_csv(path_or_buf=response, index=False)
                return response
            
            #Comparison
            form_option = request.POST.get('option', "")
            scenario_form = request.POST.get('scenario_form', "")
            scenario_form2 = request.POST.get('scenario_form2', "")
            region_form = request.POST.get('region_form', "")
            region_form2 = request.POST.get('region_form2', "")
            year_form = request.POST.get('year_form', "")
            year_form2 = request.POST.get('year_form2', "")
            comparison_datasets = []
            comparison_labels = []
            if form_option=="1":
                year="year_"+year_form
                energy_cost_form_data=energy_cost.objects.filter(Q(region=region_form) | Q(region=region_form2)).filter(Q(scenario=scenario_form))
                for i in energy_cost_form_data:
                    comparison_labels.append( i.region+" "+i.scenario+" "+year_form+" "+i.variable.split("|")[2])
                    comparison_datasets.append(getattr(i, year, None))
            elif form_option=="2":
                year="year_"+year_form
                energy_cost_form_data=energy_cost.objects.filter(Q(scenario=scenario_form)| Q(scenario=scenario_form2)).filter(Q(region=region_form))
                for i in energy_cost_form_data:
                    comparison_labels.append( i.region+" "+i.scenario+" "+year_form+" "+i.variable.split("|")[2])
                    comparison_datasets.append(getattr(i, year, None))
            else:
                year="year_"+year_form
                year2="year_"+year_form2
                energy_cost_form_data=energy_cost.objects.filter(Q(region=region_form) & Q(scenario=scenario_form))
                for i in energy_cost_form_data:
                    comparison_labels.append( i.region+" "+i.scenario+" "+year_form+" "+i.variable.split("|")[2])
                    comparison_datasets.append(getattr(i, year, None))
                    comparison_labels.append( i.region+" "+i.scenario+" "+year_form2+" "+i.variable.split("|")[2])
                    comparison_datasets.append(getattr(i, year2, None))

            return render(request,'energy_cost.html',{"scenarios":scenarios,"region":region,"variable":variable,"variable_name":variable_name,"year_first":year_first,"scenario_name":scenario_name,"region_name":region_name,"region_category":region_category,"datasets":datasets,"labels":labels,"labels_chart":labels_chart,"geojson_data":geojson_data,"scenario_map":scenario_map,"year_map":year_map[5:],"topbottom":topbottom,"topbottomn":topbottomn,"topbottom_datasets":topbottom_datasets,"energy_cost_data_table":energy_cost_data_table_main,"scenario_table":scenario_table,"region_table":region_table,"year_table":year_table,"variable_table":variable_table,"comparison_datasets":comparison_datasets,"comparison_labels":comparison_labels,"form_option":form_option,"scenario_form":scenario_form,"scenario_form2":scenario_form2,"region_form":region_form,"region_form2":region_form2,"year_form":year_form,"year_form2":year_form2})
        else:
            scenarios=energy_cost.objects.values("scenario").distinct()
            region=energy_cost.objects.values("region").distinct()
            variable = energy_cost.objects.values("variable").distinct()
            region_category = energy_cost.objects.values("region_category").distinct()
            region_category_temp_list = energy_cost.objects.values_list("region_category").distinct()
            scenario_name = request.POST.getlist('scenario',['Below 2?C','Current Policies','Delayed transition', 'Fragmented World', 'Low demand',  'Nationally Determined Contributions (NDCs)',  'Net Zero 2050'])
            region_name =  request.POST.getlist('region',["World"])
            year_first = request.POST.getlist("year_first",['2020','2025','2030','2035'])
            variable_name = request.POST.getlist("variable",['Capital Cost|Electricity|Nuclear', 'Capital Cost|Electricity|Solar|CSP', 'Capital Cost|Electricity|Coal|w/o CCS', 'Capital Cost|Electricity|Gas|w/o CCS', 'Capital Cost|Electricity|Gas|w/ CCS', 'Capital Cost|Electricity|Geothermal', 'Capital Cost|Electricity|Biomass|w/o CCS', 'Capital Cost|Electricity|Wind|Onshore', 'Capital Cost|Electricity|Biomass|w/ CCS', 'Capital Cost|Electricity|Solar|PV', 'Capital Cost|Electricity|Coal|w/ CCS', 'Capital Cost|Electricity|Wind|Offshore'])
            region_category_temp=[i[0] for i in region_category_temp_list]
            region_category_list=[]
            region_name_list=[]
            for i in region_name:
                if i in region_category_temp:
                    region_category_list.append(i)
                else:
                    region_name_list.append(i)
            if region_category_list:
                energy_cost_datasets=energy_cost.objects.filter(scenario__in=scenario_name).filter(region_category__in=region_category_list).filter(variable__in=variable_name)
                energy_cost_data=energy_cost.objects.filter(scenario__in=scenario_name).filter(region_category__in=region_category_list).filter(variable__in=variable_name).values_list(*[field.name for field in energy_cost._meta.get_fields() if field.name.startswith('year') and field.name[len(field.name)-4:] in year_first])
            else:
                energy_cost_datasets=energy_cost.objects.filter(scenario__in=scenario_name).filter(region__in=region_name_list).filter(variable__in=variable_name)
                energy_cost_data=energy_cost.objects.filter(scenario__in=scenario_name).filter(region__in=region_name_list).filter(variable__in=variable_name).values_list(*[field.name for field in energy_cost._meta.get_fields() if field.name.startswith('year') and field.name[len(field.name)-4:] in year_first])
            labels =[field.name[5:] for field in energy_cost._meta.get_fields() if field.name.startswith('year')]
            labels_chart =[i for i in [field.name[5:] for field in energy_cost._meta.get_fields() if field.name.startswith('year')] if i in year_first]
            
            datasets=[]
            for i,j in zip(energy_cost_datasets,energy_cost_data):
                datasets.append({"label": i.region+" "+i.scenario+" "+i.variable,"data":list(j),"borderColor": random_color()})
            
            #map
            queryset_main = location_data("energy")
            scenario_map = request.POST.get('scenario_map', "Net Zero 2050")
            year_map = "year_"+request.POST.get('year_map', '2100')
            geojson_data = {
                "type": "FeatureCollection",
                "features": []
            }
            queryset=queryset_main[(queryset_main["scenario"]==scenario_map)]

            for _, record in queryset.iterrows():  # Use iterrows to iterate through DataFrame rows
                feature = {
                    "type": "Feature",
                    "geometry": {
                    "type": "Point",
                    "coordinates": [record["Longitude"], record["Latitude"]],
                    },
                    "properties": {
                    "region": record["region"],         # Access fields using column names
                    "scenario": record["scenario"],
                    "year_label":year_map[5:],
                    "price_2100": record[year_map],
                    }
                }
                geojson_data["features"].append(feature)


            #top Bottom
            topbottom = request.POST.get('topbottom', "top")
            topbottomn = request.POST.get('topbottomn', '5')
            numeric_data = queryset_main.select_dtypes(include=['number'])
            queryset_main["mean"]=numeric_data.mean(axis=1)
            queryset_main = queryset_main.sort_values(by='mean', ascending=False)
            topbottom_datasets = []
            if topbottom=="top":
                queryset_main=queryset_main.head(int(topbottomn))
            else:
                queryset_main=queryset_main.tail(int(topbottomn))
            for _, record in queryset_main.iterrows():
                topbottom_datasets.append({"label": record["region"]+" "+record["scenario"],"data":record.filter(regex='^year_').values.tolist(),"borderColor": random_color()})

            #table
            energy_cost_data_table=pd.DataFrame(list(energy_cost.objects.all().values()))
            scenario_table = request.POST.getlist('scenario_table', ["Low demand"])
            region_table = request.POST.getlist('region_table', ["World"])
            year_table = request.POST.getlist('year_table', ['2025'])
            variable_table = request.POST.getlist('variable_table')
            energy_cost_data_table1=energy_cost_data_table[(energy_cost_data_table["scenario"].isin(scenario_table)) & (energy_cost_data_table["region"].isin(region_table)) & (energy_cost_data_table["variable"].isin(variable_table))]
            energy_cost_data_table2=energy_cost_data_table[(energy_cost_data_table["scenario"].isin(scenario_table)) & (energy_cost_data_table["region_category"].isin(region_table)) & (energy_cost_data_table["variable"].isin(variable_table))]
            energy_cost_data_table = pd.concat([energy_cost_data_table1, energy_cost_data_table2], ignore_index=True)
            energy_cost_data_table=energy_cost_data_table[["scenario","region_category","region","unit","variable"]+["year_"+i for i in year_table]]
            energy_cost_data_table_year=energy_cost_data_table[[col for col in energy_cost_data_table.columns if col.startswith('year')]].values.tolist()
            energy_cost_data_table_main=[]
            for i in range(len(energy_cost_data_table)):
                energy_cost_data_table_main.append({"srno":i+1,"scenario":energy_cost_data_table["scenario"][i],"region_category":energy_cost_data_table["region_category"][i],"region":energy_cost_data_table["region"][i],"unit":energy_cost_data_table["unit"][i],"variable":energy_cost_data_table["variable"][i],"year":energy_cost_data_table_year[i]})

            return render(request,'energy_cost.html',{"scenarios":scenarios,"region":region,"variable":variable,"year_first":year_first,"variable_name":variable_name,"scenario_name":scenario_name,"region_name":region_name,"region_category":region_category,"datasets":datasets,"labels":labels,"labels_chart":labels_chart,"geojson_data":geojson_data,"scenario_map":scenario_map,"year_map":year_map[5:],"topbottom":topbottom,"topbottomn":topbottomn,"topbottom_datasets":topbottom_datasets,"energy_cost_data_table":energy_cost_data_table_main,"scenario_table":scenario_table,"region_table":region_table,"year_table":year_table,"variable_table":variable_table})
    else:
        return redirect('/')


def emmission_pathways(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            scenarios=co2_emission.objects.values("scenario").distinct()
            region=co2_emission.objects.values("region").distinct()
            region_category = co2_emission.objects.values("region_category").distinct()
            region_category_temp_list = co2_emission.objects.values_list("region_category").distinct()
            scenario_name = request.POST.getlist('scenario',['Below 2?C','Current Policies','Delayed transition', 'Fragmented World', 'Low demand',  'Nationally Determined Contributions (NDCs)',  'Net Zero 2050'])
            region_name =  request.POST.getlist('region',["World"])
            year_first = request.POST.getlist("year_first",['2020','2025','2030','2035'])
            region_category_temp=[i[0] for i in region_category_temp_list]
            region_category_list=[]
            region_name_list=[]
            for i in region_name:
                if i in region_category_temp:
                    region_category_list.append(i)
                else:
                    region_name_list.append(i)
            if region_category_list:
                co2_emission_datasets=co2_emission.objects.filter(scenario__in=scenario_name).filter(region_category__in=region_category_list)
                co2_emission_data=co2_emission.objects.filter(scenario__in=scenario_name).filter(region_category__in=region_category_list).values_list(*[field.name for field in co2_emission._meta.get_fields() if field.name.startswith('year') and field.name[len(field.name)-4:] in year_first])
            else:
                co2_emission_datasets=co2_emission.objects.filter(scenario__in=scenario_name).filter(region__in=region_name_list)
                co2_emission_data=co2_emission.objects.filter(scenario__in=scenario_name).filter(region__in=region_name_list).values_list(*[field.name for field in co2_emission._meta.get_fields() if field.name.startswith('year') and field.name[len(field.name)-4:] in year_first])
            labels = [field.name[5:] for field in co2_emission._meta.get_fields() if field.name.startswith('year')]
            labels_chart =[i for i in [field.name[5:] for field in co2_emission._meta.get_fields() if field.name.startswith('year')] if i in year_first]

            datasets = []
            for i,j in zip(co2_emission_datasets,co2_emission_data):
                datasets.append({"label": i.region+" "+i.scenario,"data":list(j),"borderColor": random_color()})

            #map
            queryset_main = location_data("co2")
            scenario_map = request.POST.get('scenario_map', "Net Zero 2050")
            year_map = "year_"+request.POST.get('year_map', '2100')
            queryset=queryset_main[queryset_main["scenario"]==scenario_map]
            geojson_data = {
                "type": "FeatureCollection",
                "features": []
            }

            for _, record in queryset.iterrows():  # Use iterrows to iterate through DataFrame rows
                feature = {
                    "type": "Feature",
                    "geometry": {
                    "type": "Point",
                    "coordinates": [record["Longitude"], record["Latitude"]],
                    },
                    "properties": {
                    "region": record["region"],         # Access fields using column names
                    "scenario": record["scenario"],
                    "year_label":year_map[5:],
                    "price_2100": record[year_map],
                    }
                }
                geojson_data["features"].append(feature)
                
            #top Bottom
            topbottom = request.POST.get('topbottom', "top")
            topbottomn = request.POST.get('topbottomn', '5')
            numeric_data = queryset_main.select_dtypes(include=['number'])
            queryset_main["mean"]=numeric_data.mean(axis=1)
            queryset_main = queryset_main.sort_values(by='mean', ascending=False)
            topbottom_datasets = []
            if topbottom=="top":
                queryset_main=queryset_main.head(int(topbottomn))
            else:
                queryset_main=queryset_main.tail(int(topbottomn))
            for _, record in queryset_main.iterrows():
                topbottom_datasets.append({"label": record["region"]+" "+record["scenario"],"data":record.filter(regex='^year_').values.tolist(),"borderColor": random_color()})

            #table
            co2_emission_data_table=pd.DataFrame(list(co2_emission.objects.all().values()))
            scenario_table = request.POST.getlist('scenario_table', ["Low demand"])
            region_table = request.POST.getlist('region_table', ["World"])
            year_table = request.POST.getlist('year_table', ['2025'])
            co2_emission_data_table1=co2_emission_data_table[(co2_emission_data_table["scenario"].isin(scenario_table)) & (co2_emission_data_table["region"].isin(region_table))]
            co2_emission_data_table2=co2_emission_data_table[(co2_emission_data_table["scenario"].isin(scenario_table)) & (co2_emission_data_table["region_category"].isin(region_table))]
            co2_emission_data_table = pd.concat([co2_emission_data_table1, co2_emission_data_table2], ignore_index=True)
            co2_emission_data_table=co2_emission_data_table[["scenario","region_category","region","unit"]+["year_"+i for i in year_table]]
            co2_emission_data_table_year=co2_emission_data_table[[col for col in co2_emission_data_table.columns if col.startswith('year')]].values.tolist()
            co2_emission_data_table_main=[]
            for i in range(len(co2_emission_data_table)):
                co2_emission_data_table_main.append({"srno":i+1,"scenario":co2_emission_data_table["scenario"][i],"region_category":co2_emission_data_table["region_category"][i],"region":co2_emission_data_table["region"][i],"unit":co2_emission_data_table["unit"][i],"year":co2_emission_data_table_year[i]})
            #export
            if "export" in request.POST:
                response = HttpResponse(content_type='text/csv')
                response['Content-Disposition'] = 'attachment; filename="data.csv"'
                co2_emission_data_table.to_csv(path_or_buf=response, index=False)
                return response
            
            #Comparison
            form_option = request.POST.get('option', "")
            scenario_form = request.POST.get('scenario_form', "")
            scenario_form2 = request.POST.get('scenario_form2', "")
            region_form = request.POST.get('region_form', "")
            region_form2 = request.POST.get('region_form2', "")
            year_form = request.POST.get('year_form', "")
            year_form2 = request.POST.get('year_form2', "")
            comparison_datasets = []
            comparison_labels = []
            if form_option=="1":
                year="year_"+year_form
                co2_emission_form_data=co2_emission.objects.filter(Q(region=region_form) | Q(region=region_form2)).filter(Q(scenario=scenario_form))
                for i in co2_emission_form_data:
                    comparison_labels.append( i.region+" "+i.scenario+" "+year_form)
                    comparison_datasets.append(getattr(i, year, None))
            elif form_option=="2":
                year="year_"+year_form
                co2_emission_form_data=co2_emission.objects.filter(Q(scenario=scenario_form)| Q(scenario=scenario_form2)).filter(Q(region=region_form))
                for i in co2_emission_form_data:
                    comparison_labels.append( i.region+" "+i.scenario+" "+year_form)
                    comparison_datasets.append(getattr(i, year, None))
            else:
                year="year_"+year_form
                year2="year_"+year_form2
                co2_emission_form_data=co2_emission.objects.filter(Q(region=region_form) & Q(scenario=scenario_form))
                for i in co2_emission_form_data:
                    comparison_labels.append( i.region+" "+i.scenario+" "+year_form)
                    comparison_datasets.append(getattr(i, year, None))
                    comparison_labels.append( i.region+" "+i.scenario+" "+year_form2)
                    comparison_datasets.append(getattr(i, year2, None))
            return render(request,'emmission_pathways.html',{"scenarios":scenarios,"region":region,"year_first":year_first,"scenario_name":scenario_name,"region_name":region_name,"region_category":region_category,"datasets":datasets,"labels":labels,"labels_chart":labels_chart,"geojson_data":geojson_data,"scenario_map":scenario_map,"year_map":year_map[5:],"topbottom":topbottom,"topbottomn":topbottomn,"topbottom_datasets":topbottom_datasets,"energy_cost_data_table":co2_emission_data_table_main,"scenario_table":scenario_table,"region_table":region_table,"year_table":year_table,"comparison_datasets":comparison_datasets,"comparison_labels":comparison_labels,"form_option":form_option,"scenario_form":scenario_form,"scenario_form2":scenario_form2,"region_form":region_form,"region_form2":region_form2,"year_form":year_form,"year_form2":year_form2})
        else:
            scenarios=co2_emission.objects.values('scenario').distinct()
            region=co2_emission.objects.values("region").distinct()
            region_category = co2_emission.objects.values("region_category").distinct()
            region_category_temp_list = co2_emission.objects.values_list("region_category").distinct()
            scenario_name = request.POST.getlist('scenario',['Below 2?C','Current Policies','Delayed transition', 'Fragmented World', 'Low demand',  'Nationally Determined Contributions (NDCs)',  'Net Zero 2050'])
            region_name =  request.POST.getlist('region',["World"])
            year_first = request.POST.getlist("year_first",['2020','2025','2030','2035'])
            region_category_temp=[i[0] for i in region_category_temp_list]
            region_category_list=[]
            region_name_list=[]
            for i in region_name:
                if i in region_category_temp:
                    region_category_list.append(i)
                else:
                    region_name_list.append(i)
            if region_category_list:
                corban_pricing_datasets=co2_emission.objects.filter(scenario__in=scenario_name).filter(region_category__in=region_category_list)
                corban_pricing_data=co2_emission.objects.filter(scenario__in=scenario_name).filter(region_category__in=region_category_list).values_list(*[field.name for field in co2_emission._meta.get_fields() if field.name.startswith('year') and field.name[len(field.name)-4:] in year_first])
            else:
                corban_pricing_datasets=co2_emission.objects.filter(scenario__in=scenario_name).filter(region__in=region_name_list)
                corban_pricing_data=co2_emission.objects.filter(scenario__in=scenario_name).filter(region__in=region_name_list).values_list(*[field.name for field in co2_emission._meta.get_fields() if field.name.startswith('year') and field.name[len(field.name)-4:] in year_first])
            labels = [field.name[5:] for field in co2_emission._meta.get_fields() if field.name.startswith('year')]
            labels_chart =[i for i in [field.name[5:] for field in co2_emission._meta.get_fields() if field.name.startswith('year')] if i in year_first]

            datasets = []
            for i,j in zip(corban_pricing_datasets,corban_pricing_data):
                datasets.append({"label": i.region+" "+i.scenario,"data":list(j),"borderColor": random_color()})
            
            #map
            queryset_main = location_data("co2")
            scenario_map = request.POST.get('scenario_map', "Net Zero 2050")
            year_map = "year_"+request.POST.get('year_map', '2100')
            geojson_data = {
                "type": "FeatureCollection",
                "features": []
            }
            queryset=queryset_main[(queryset_main["scenario"]==scenario_map)]

            for _, record in queryset.iterrows():  # Use iterrows to iterate through DataFrame rows
                feature = {
                    "type": "Feature",
                    "geometry": {
                    "type": "Point",
                    "coordinates": [record["Longitude"], record["Latitude"]],
                    },
                    "properties": {
                    "region": record["region"],         # Access fields using column names
                    "scenario": record["scenario"],
                    "year_label":year_map[5:],
                    "price_2100": record[year_map],
                    }
                }
                geojson_data["features"].append(feature)


            #top Bottom
            topbottom = request.POST.get('topbottom', "top")
            topbottomn = request.POST.get('topbottomn', '5')
            numeric_data = queryset_main.select_dtypes(include=['number'])
            queryset_main["mean"]=numeric_data.mean(axis=1)
            queryset_main = queryset_main.sort_values(by='mean', ascending=False)
            topbottom_datasets = []
            if topbottom=="top":
                queryset_main=queryset_main.head(int(topbottomn))
            else:
                queryset_main=queryset_main.tail(int(topbottomn))
            for _, record in queryset_main.iterrows():
                topbottom_datasets.append({"label": record["region"]+" "+record["scenario"],"data":record.filter(regex='^year_').values.tolist(),"borderColor": random_color()})

            #table
            corban_pricing_data_table=pd.DataFrame(list(co2_emission.objects.all().values()))
            scenario_table = request.POST.getlist('scenario_table', ["Low demand"])
            region_table = request.POST.getlist('region_table', ["World"])
            year_table = request.POST.getlist('year_table', ['2025'])
            corban_pricing_data_table1=corban_pricing_data_table[(corban_pricing_data_table["scenario"].isin(scenario_table)) & (corban_pricing_data_table["region"].isin(region_table))]
            corban_pricing_data_table2=corban_pricing_data_table[(corban_pricing_data_table["scenario"].isin(scenario_table)) & (corban_pricing_data_table["region_category"].isin(region_table))]
            corban_pricing_data_table = pd.concat([corban_pricing_data_table1, corban_pricing_data_table2], ignore_index=True)
            corban_pricing_data_table=corban_pricing_data_table[["scenario","region_category","region","unit"]+["year_"+i for i in year_table]]
            corban_pricing_data_table_year=corban_pricing_data_table[[col for col in corban_pricing_data_table.columns if col.startswith('year')]].values.tolist()
            corban_pricing_data_table_main=[]
            for i in range(len(corban_pricing_data_table)):
                corban_pricing_data_table_main.append({"srno":i+1,"scenario":corban_pricing_data_table["scenario"][i],"region_category":corban_pricing_data_table["region_category"][i],"region":corban_pricing_data_table["region"][i],"unit":corban_pricing_data_table["unit"][i],"year":corban_pricing_data_table_year[i]})
            
            return render(request,'emmission_pathways.html',{"scenarios":scenarios,"region":region,"year_first":year_first,"scenario_name":scenario_name,"region_name":region_name,"region_category":region_category,"datasets":datasets,"labels":labels,"labels_chart":labels_chart,"geojson_data":geojson_data,"scenario_map":scenario_map,"year_map":year_map[5:],"topbottom":topbottom,"topbottomn":topbottomn,"topbottom_datasets":topbottom_datasets,"corban_pricing_data_table":corban_pricing_data_table_main,"scenario_table":scenario_table,"region_table":region_table,"year_table":year_table})
    else:
        return redirect('/')

def economic_forecast1(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            scenarios=economic_forecast.objects.values("scenario").distinct()
            region=economic_forecast.objects.values("region").distinct()
            region_category = economic_forecast.objects.values("region_category").distinct()
            region_category_temp_list = economic_forecast.objects.values_list("region_category").distinct()
            scenario_name = request.POST.getlist('scenario',['Below 2?C','Current Policies','Delayed transition', 'Fragmented World', 'Low demand',  'Nationally Determined Contributions (NDCs)',  'Net Zero 2050'])
            region_name =  request.POST.getlist('region',["World"])
            year_first = request.POST.getlist("year_first",['2020','2025','2030','2035'])
            region_category_temp=[i[0] for i in region_category_temp_list]
            region_category_list=[]
            region_name_list=[]
            for i in region_name:
                if i in region_category_temp:
                    region_category_list.append(i)
                else:
                    region_name_list.append(i)
            if region_category_list:
                economic_forecast_datasets=economic_forecast.objects.filter(scenario__in=scenario_name).filter(region_category__in=region_category_list)
                economic_forecast_data=economic_forecast.objects.filter(scenario__in=scenario_name).filter(region_category__in=region_category_list).values_list(*[field.name for field in economic_forecast._meta.get_fields() if field.name.startswith('year') and field.name[len(field.name)-4:] in year_first])
            else:
                economic_forecast_datasets=economic_forecast.objects.filter(scenario__in=scenario_name).filter(region__in=region_name_list)
                economic_forecast_data=economic_forecast.objects.filter(scenario__in=scenario_name).filter(region__in=region_name_list).values_list(*[field.name for field in economic_forecast._meta.get_fields() if field.name.startswith('year') and field.name[len(field.name)-4:] in year_first])
            labels = [field.name[5:] for field in economic_forecast._meta.get_fields() if field.name.startswith('year')]
            labels_chart =[i for i in [field.name[5:] for field in economic_forecast._meta.get_fields() if field.name.startswith('year')] if i in year_first]
            datasets = []
            for i,j in zip(economic_forecast_datasets,economic_forecast_data):
                datasets.append({"label": i.region+" "+i.scenario,"data":list(j),"borderColor": random_color()})

            #map
            queryset_main = location_data("economic")
            scenario_map = request.POST.get('scenario_map', "Net Zero 2050")
            year_map = "year_"+request.POST.get('year_map', '2100')
            queryset=queryset_main[queryset_main["scenario"]==scenario_map]
            geojson_data = {
                "type": "FeatureCollection",
                "features": []
            }

            for _, record in queryset.iterrows():  # Use iterrows to iterate through DataFrame rows
                feature = {
                    "type": "Feature",
                    "geometry": {
                    "type": "Point",
                    "coordinates": [record["Longitude"], record["Latitude"]],
                    },
                    "properties": {
                    "region": record["region"],         # Access fields using column names
                    "scenario": record["scenario"],
                    "year_label":year_map[5:],
                    "price_2100": record[year_map],
                    }
                }
                geojson_data["features"].append(feature)
                
            #top Bottom
            topbottom = request.POST.get('topbottom', "top")
            topbottomn = request.POST.get('topbottomn', '5')
            numeric_data = queryset_main.select_dtypes(include=['number'])
            queryset_main["mean"]=numeric_data.mean(axis=1)
            queryset_main = queryset_main.sort_values(by='mean', ascending=False)
            topbottom_datasets = []
            if topbottom=="top":
                queryset_main=queryset_main.head(int(topbottomn))
            else:
                queryset_main=queryset_main.tail(int(topbottomn))
            for _, record in queryset_main.iterrows():
                topbottom_datasets.append({"label": record["region"]+" "+record["scenario"],"data":record.filter(regex='^year_').values.tolist(),"borderColor": random_color()})

            #table
            economic_forecast_data_table=pd.DataFrame(list(economic_forecast.objects.all().values()))
            scenario_table = request.POST.getlist('scenario_table', ["Low demand"])
            region_table = request.POST.getlist('region_table', ["World"])
            year_table = request.POST.getlist('year_table', ['2025'])
            economic_forecast_data_table1=economic_forecast_data_table[(economic_forecast_data_table["scenario"].isin(scenario_table)) & (economic_forecast_data_table["region"].isin(region_table))]
            economic_forecast_data_table2=economic_forecast_data_table[(economic_forecast_data_table["scenario"].isin(scenario_table)) & (economic_forecast_data_table["region_category"].isin(region_table))]
            economic_forecast_data_table = pd.concat([economic_forecast_data_table1, economic_forecast_data_table2], ignore_index=True)
            economic_forecast_data_table=economic_forecast_data_table[["scenario","region_category","region","unit"]+["year_"+i for i in year_table]]
            economic_forecast_data_table_year=economic_forecast_data_table[[col for col in economic_forecast_data_table.columns if col.startswith('year')]].values.tolist()
            economic_forecast_data_table_main=[]
            for i in range(len(economic_forecast_data_table)):
                economic_forecast_data_table_main.append({"srno":i+1,"scenario":economic_forecast_data_table["scenario"][i],"region_category":economic_forecast_data_table["region_category"][i],"region":economic_forecast_data_table["region"][i],"unit":economic_forecast_data_table["unit"][i],"year":economic_forecast_data_table_year[i]})
            #export
            if "export" in request.POST:
                response = HttpResponse(content_type='text/csv')
                response['Content-Disposition'] = 'attachment; filename="data.csv"'
                economic_forecast_data_table.to_csv(path_or_buf=response, index=False)
                return response
            #Comparison
            form_option = request.POST.get('option', "")
            scenario_form = request.POST.get('scenario_form', "")
            scenario_form2 = request.POST.get('scenario_form2', "")
            region_form = request.POST.get('region_form', "")
            region_form2 = request.POST.get('region_form2', "")
            year_form = request.POST.get('year_form', "")
            year_form2 = request.POST.get('year_form2', "")
            comparison_datasets = []
            comparison_labels = []
            if form_option=="1":
                year="year_"+year_form
                economic_forecast_form_data=economic_forecast.objects.filter(Q(region=region_form) | Q(region=region_form2)).filter(Q(scenario=scenario_form))
                for i in economic_forecast_form_data:
                    comparison_labels.append( i.region+" "+i.scenario+" "+year_form)
                    comparison_datasets.append(getattr(i, year, None))
            elif form_option=="2":
                year="year_"+year_form
                economic_forecast_form_data=economic_forecast.objects.filter(Q(scenario=scenario_form)| Q(scenario=scenario_form2)).filter(Q(region=region_form))
                for i in economic_forecast_form_data:
                    comparison_labels.append( i.region+" "+i.scenario+" "+year_form)
                    comparison_datasets.append(getattr(i, year, None))
            else:
                year="year_"+year_form
                year2="year_"+year_form2
                economic_forecast_form_data=economic_forecast.objects.filter(Q(region=region_form) & Q(scenario=scenario_form))
                for i in economic_forecast_form_data:
                    comparison_labels.append( i.region+" "+i.scenario+" "+year_form)
                    comparison_datasets.append(getattr(i, year, None))
                    comparison_labels.append( i.region+" "+i.scenario+" "+year_form2)
                    comparison_datasets.append(getattr(i, year2, None))
            return render(request,'economic_forecast.html',{"scenarios":scenarios,"region":region,"year_first":year_first,"scenario_name":scenario_name,"region_name":region_name,"region_category":region_category,"datasets":datasets,"labels":labels,"labels_chart":labels_chart,"geojson_data":geojson_data,"scenario_map":scenario_map,"year_map":year_map[5:],"topbottom":topbottom,"topbottomn":topbottomn,"topbottom_datasets":topbottom_datasets,"corban_pricing_data_table":economic_forecast_data_table_main,"scenario_table":scenario_table,"region_table":region_table,"year_table":year_table,"comparison_datasets":comparison_datasets,"comparison_labels":comparison_labels,"form_option":form_option,"scenario_form":scenario_form,"scenario_form2":scenario_form2,"region_form":region_form,"region_form2":region_form2,"year_form":year_form,"year_form2":year_form2})
        else:
            scenarios=economic_forecast.objects.values('scenario').distinct()
            region=economic_forecast.objects.values("region").distinct()
            region_category = economic_forecast.objects.values("region_category").distinct()
            region_category_temp_list = economic_forecast.objects.values_list("region_category").distinct()
            scenario_name = request.POST.getlist('scenario',['Below 2?C','Current Policies','Delayed transition', 'Fragmented World', 'Low demand',  'Nationally Determined Contributions (NDCs)',  'Net Zero 2050'])
            region_name =  request.POST.getlist('region',["World"])
            year_first = request.POST.getlist("year_first",['2020','2025','2030','2035'])
            region_category_temp=[i[0] for i in region_category_temp_list]
            region_category_list=[]
            region_name_list=[]
            for i in region_name:
                if i in region_category_temp:
                    region_category_list.append(i)
                else:
                    region_name_list.append(i)
            if region_category_list:
                corban_pricing_datasets=economic_forecast.objects.filter(scenario__in=scenario_name).filter(region_category__in=region_category_list)
                corban_pricing_data=economic_forecast.objects.filter(scenario__in=scenario_name).filter(region_category__in=region_category_list).values_list(*[field.name for field in economic_forecast._meta.get_fields() if field.name.startswith('year') and field.name[len(field.name)-4:] in year_first])
            else:
                corban_pricing_datasets=economic_forecast.objects.filter(scenario__in=scenario_name).filter(region__in=region_name_list)
                corban_pricing_data=economic_forecast.objects.filter(scenario__in=scenario_name).filter(region__in=region_name_list).values_list(*[field.name for field in economic_forecast._meta.get_fields() if field.name.startswith('year') and field.name[len(field.name)-4:] in year_first])
            labels = [field.name[5:] for field in economic_forecast._meta.get_fields() if field.name.startswith('year')]
            labels_chart =[i for i in [field.name[5:] for field in economic_forecast._meta.get_fields() if field.name.startswith('year')] if i in year_first]
            datasets = []
            for i,j in zip(corban_pricing_datasets,corban_pricing_data):
                datasets.append({"label": i.region+" "+i.scenario,"data":list(j),"borderColor": random_color()})
            
            #map
            queryset_main = location_data("economic")
            scenario_map = request.POST.get('scenario_map', "Net Zero 2050")
            year_map = "year_"+request.POST.get('year_map', '2100')
            geojson_data = {
                "type": "FeatureCollection",
                "features": []
            }
            queryset=queryset_main[(queryset_main["scenario"]==scenario_map)]

            for _, record in queryset.iterrows():  # Use iterrows to iterate through DataFrame rows
                feature = {
                    "type": "Feature",
                    "geometry": {
                    "type": "Point",
                    "coordinates": [record["Longitude"], record["Latitude"]],
                    },
                    "properties": {
                    "region": record["region"],         # Access fields using column names
                    "scenario": record["scenario"],
                    "year_label":year_map[5:],
                    "price_2100": record[year_map],
                    }
                }
                geojson_data["features"].append(feature)


            #top Bottom
            topbottom = request.POST.get('topbottom', "top")
            topbottomn = request.POST.get('topbottomn', '5')
            numeric_data = queryset_main.select_dtypes(include=['number'])
            queryset_main["mean"]=numeric_data.mean(axis=1)
            queryset_main = queryset_main.sort_values(by='mean', ascending=False)
            topbottom_datasets = []
            if topbottom=="top":
                queryset_main=queryset_main.head(int(topbottomn))
            else:
                queryset_main=queryset_main.tail(int(topbottomn))
            for _, record in queryset_main.iterrows():
                topbottom_datasets.append({"label": record["region"]+" "+record["scenario"],"data":record.filter(regex='^year_').values.tolist(),"borderColor": random_color()})

            #table
            corban_pricing_data_table=pd.DataFrame(list(economic_forecast.objects.all().values()))
            scenario_table = request.POST.getlist('scenario_table', ["Low demand"])
            region_table = request.POST.getlist('region_table', ["World"])
            year_table = request.POST.getlist('year_table', ['2025'])
            corban_pricing_data_table1=corban_pricing_data_table[(corban_pricing_data_table["scenario"].isin(scenario_table)) & (corban_pricing_data_table["region"].isin(region_table))]
            corban_pricing_data_table2=corban_pricing_data_table[(corban_pricing_data_table["scenario"].isin(scenario_table)) & (corban_pricing_data_table["region_category"].isin(region_table))]
            corban_pricing_data_table = pd.concat([corban_pricing_data_table1, corban_pricing_data_table2], ignore_index=True)
            corban_pricing_data_table=corban_pricing_data_table[["scenario","region_category","region","unit"]+["year_"+i for i in year_table]]
            corban_pricing_data_table_year=corban_pricing_data_table[[col for col in corban_pricing_data_table.columns if col.startswith('year')]].values.tolist()
            corban_pricing_data_table_main=[]
            for i in range(len(corban_pricing_data_table)):
                corban_pricing_data_table_main.append({"srno":i+1,"scenario":corban_pricing_data_table["scenario"][i],"region_category":corban_pricing_data_table["region_category"][i],"region":corban_pricing_data_table["region"][i],"unit":corban_pricing_data_table["unit"][i],"year":corban_pricing_data_table_year[i]})
            return render(request,'economic_forecast.html',{"scenarios":scenarios,"region":region,"year_first":year_first,"scenario_name":scenario_name,"region_name":region_name,"region_category":region_category,"datasets":datasets,"labels":labels,"labels_chart":labels_chart,"geojson_data":geojson_data,"scenario_map":scenario_map,"year_map":year_map[5:],"topbottom":topbottom,"topbottomn":topbottomn,"topbottom_datasets":topbottom_datasets,"corban_pricing_data_table":corban_pricing_data_table_main,"scenario_table":scenario_table,"region_table":region_table,"year_table":year_table})
    else:
        return redirect('/')


























































