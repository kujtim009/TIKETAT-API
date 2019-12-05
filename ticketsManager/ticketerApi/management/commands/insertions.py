from django.core.management.base import BaseCommand, CommandError
from  ticketerApi.models import Regjionet, Reshtat, Ulset, Cmimet, Shitja
from ticketerApi.cordinates import cordinates




class Command(BaseCommand):
    help = 'insertAll'
    

    def handle(self, *args, **options):
        # myArray = [d for i,d in enumerate(cordinates) if 'P101' in d['regionId'] and 'A' in d['rowID'] and d['sitId'] == 2]
        # str1 = ''.join(str(myArray[0]['cords']))
        # print(str1)
        regjions = Regjionet(emri='P101', hyrja='B')
        regjions.save()
        regjions = Regjionet(emri='P102', hyrja='B')
        regjions.save()
        regjions = Regjionet(emri='P103', hyrja='C')
        regjions.save()
        regjions = Regjionet(emri='L109', hyrja='A')
        regjions.save()
        regjions = Regjionet(emri='L110', hyrja='A')
        regjions.save()
        regjions = Regjionet(emri='L111', hyrja='A')
        regjions.save()
        regjions = Regjionet(emri='V112', hyrja='A')
        regjions.save()
        regjions = Regjionet(emri='V113', hyrja='B')
        regjions.save()
        regjions = Regjionet(emri='J104', hyrja='C')
        regjions.save()
        regjions = Regjionet(emri='J105', hyrja='C')
        regjions.save()
        regjions = Regjionet(emri='J106', hyrja='C')
        regjions.save()
        regjions = Regjionet(emri='J107', hyrja='C')
        regjions.save()
        regjions = Regjionet(emri='J108', hyrja='C')
        regjions.save()

        regjions = Regjionet(emri='VIP1', hyrja='ABC')
        regjions.save()

        regjions = Regjionet(emri='VIP2', hyrja='ABC')
        regjions.save()

        regjions = Regjionet(emri='VIP3', hyrja='ABC')
        regjions.save()

        regjions = Regjionet(emri='VIP4', hyrja='ABC')
        regjions.save()

        regjions = Regjionet(emri='KMB', hyrja='ABC')
        regjions.save()
        
        
        reshtat = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N']
        for resht in reshtat:
            insert1 = Reshtat(emri=resht)
            insert1.save()
        # reshtat = ['A','B']

        regjioni = Regjionet.objects.filter(emri="P101")[0]

        for resht in reshtat:
            reshti = Reshtat.objects.filter(emri=resht)[0]
            insert1 = Cmimet(regjioni=regjioni, reshti=reshti, cmimi=1)
            insert1.save()

        for resht in reshtat:
            for ulsa in range(1, 26):
                myArray = [d for i,d in enumerate(cordinates) if 'P101' in d['regionId'] and resht in d['rowID'] and d['sitId'] == ulsa]
                try:
                    str1 = ''.join(str(myArray[0]['cords']))
                except:
                    str1 = ""
                
                reshti = Reshtat.objects.filter(emri=resht)[0]
                insert1 = Ulset(regjioni=regjioni, reshti=reshti, ulsa=ulsa, statusi=False, cordinata=str1)
                insert1.save()


        regjioni = Regjionet.objects.filter(emri="P103")[0]
        for resht in reshtat:
            reshti = Reshtat.objects.filter(emri=resht)[0]
            insert1 = Cmimet(regjioni=regjioni, reshti=reshti, cmimi=1)
            insert1.save()
        for resht in reshtat:
            for ulsa in range(1, 26):
                myArray = [d for i,d in enumerate(cordinates) if 'P103' in d['regionId'] and resht in d['rowID'] and d['sitId'] == ulsa]
                try:
                    str1 = ''.join(str(myArray[0]['cords']))
                except:
                    str1 = ""
                reshti = Reshtat.objects.filter(emri=resht)[0]
                insert1 = Ulset(regjioni=regjioni, reshti=reshti, ulsa=ulsa, statusi=False, cordinata=str1)
                insert1.save()



        regjioni = Regjionet.objects.filter(emri="P102")[0]
        for resht in reshtat:
            reshti = Reshtat.objects.filter(emri=resht)[0]
            insert1 = Cmimet(regjioni=regjioni, reshti=reshti, cmimi=1)
            insert1.save()
        for resht in reshtat:
            for ulsa in range(1, 31):
                myArray = [d for i,d in enumerate(cordinates) if 'P102' in d['regionId'] and resht in d['rowID'] and d['sitId'] == ulsa]
                try:
                    str1 = ''.join(str(myArray[0]['cords']))
                except:
                    str1 = ""
                reshti = Reshtat.objects.filter(emri=resht)[0]
                insert1 = Ulset(regjioni=regjioni, reshti=reshti, ulsa=ulsa, statusi=False, cordinata=str1)
                insert1.save()


        reshtat = ['A','B','C','D','E','F','G']
        regjioni = Regjionet.objects.filter(emri="L111")[0]
        for resht in reshtat:
            reshti = Reshtat.objects.filter(emri=resht)[0]
            insert1 = Cmimet(regjioni=regjioni, reshti=reshti, cmimi=1)
            insert1.save()
        for resht in reshtat:
            for ulsa in range(1, 26):
                myArray = [d for i,d in enumerate(cordinates) if 'L111' in d['regionId'] and resht in d['rowID'] and d['sitId'] == ulsa]
                try:
                    str1 = ''.join(str(myArray[0]['cords']))
                except:
                    str1 = ""
                if resht == "G" and ulsa >= 18:
                    break
                reshti = Reshtat.objects.filter(emri=resht)[0]
                insert1 = Ulset(regjioni=regjioni, reshti=reshti, ulsa=ulsa, statusi=False, cordinata=str1)
                insert1.save()

        reshtat = ['A','B','C','D','E','F']
        regjioni = Regjionet.objects.filter(emri="L110")[0]
        for resht in reshtat:
            reshti = Reshtat.objects.filter(emri=resht)[0]
            insert1 = Cmimet(regjioni=regjioni, reshti=reshti, cmimi=1)
            insert1.save()
        for resht in reshtat:
            for ulsa in range(1, 31):
                myArray = [d for i,d in enumerate(cordinates) if 'L110' in d['regionId'] and resht in d['rowID'] and d['sitId'] == ulsa]
                try:
                    str1 = ''.join(str(myArray[0]['cords']))
                except:
                    str1 = ""
                if ulsa >= 23 and resht == "C":
                    break

                if ulsa >= 23 and resht == "D":
                    break
                
                if ulsa >= 22 and resht == "E":
                    break

                if ulsa >= 11 and resht == "F":
                    break

                reshti = Reshtat.objects.filter(emri=resht)[0]
                insert1 = Ulset(regjioni=regjioni, reshti=reshti, ulsa=ulsa, statusi=False, cordinata=str1)
                insert1.save()


        
        reshtat = ['A','B','C','D']
        regjioni = Regjionet.objects.filter(emri="L109")[0]
        for resht in reshtat:
            reshti = Reshtat.objects.filter(emri=resht)[0]
            insert1 = Cmimet(regjioni=regjioni, reshti=reshti, cmimi=1)
            insert1.save()
        for resht in reshtat:
            for ulsa in range(1, 26):
                myArray = [d for i,d in enumerate(cordinates) if 'L109' in d['regionId'] and resht in d['rowID'] and d['sitId'] == ulsa]
                try:
                    str1 = ''.join(str(myArray[0]['cords']))
                except:
                    str1 = ""
                if ulsa >= 17 and resht == "D":
                    break
                reshti = Reshtat.objects.filter(emri=resht)[0]
                insert1 = Ulset(regjioni=regjioni, reshti=reshti, ulsa=ulsa, statusi=False, cordinata=str1)
                insert1.save()


        reshtat = ['A','B','C']
        regjioni = Regjionet.objects.filter(emri="V112")[0]
        for resht in reshtat:
            reshti = Reshtat.objects.filter(emri=resht)[0]
            insert1 = Cmimet(regjioni=regjioni, reshti=reshti, cmimi=1)
            insert1.save()
        for resht in reshtat:
            for ulsa in range(1, 22):
                myArray = [d for i,d in enumerate(cordinates) if 'V112' in d['regionId'] and resht in d['rowID'] and d['sitId'] == ulsa]
                try:
                    str1 = ''.join(str(myArray[0]['cords']))
                except:
                    str1 = ""
                reshti = Reshtat.objects.filter(emri=resht)[0]
                insert1 = Ulset(regjioni=regjioni, reshti=reshti, ulsa=ulsa, statusi=False, cordinata=str1)
                insert1.save()


        reshtat = ['A','B','C']
        regjioni = Regjionet.objects.filter(emri="V113")[0]
        for resht in reshtat:
            reshti = Reshtat.objects.filter(emri=resht)[0]
            insert1 = Cmimet(regjioni=regjioni, reshti=reshti, cmimi=1)
            insert1.save()
        for resht in reshtat:
            for ulsa in range(1, 22):
                myArray = [d for i,d in enumerate(cordinates) if 'V113' in d['regionId'] and resht in d['rowID'] and d['sitId'] == ulsa]
                try:
                    str1 = ''.join(str(myArray[0]['cords']))
                except:
                    str1 = ""
                reshti = Reshtat.objects.filter(emri=resht)[0]
                insert1 = Ulset(regjioni=regjioni, reshti=reshti, ulsa=ulsa, statusi=False, cordinata=str1)
                insert1.save()





        reshtat = ['A','B','C']
        regjioni = Regjionet.objects.filter(emri="J104")[0]
        for resht in reshtat:
            reshti = Reshtat.objects.filter(emri=resht)[0]
            insert1 = Cmimet(regjioni=regjioni, reshti=reshti, cmimi=1)
            insert1.save()
        for resht in reshtat:
            for ulsa in range(1, 22):
                myArray = [d for i,d in enumerate(cordinates) if 'J104' in d['regionId'] and resht in d['rowID'] and d['sitId'] == ulsa]
                try:
                    str1 = ''.join(str(myArray[0]['cords']))
                except:
                    str1 = ""
                reshti = Reshtat.objects.filter(emri=resht)[0]
                insert1 = Ulset(regjioni=regjioni, reshti=reshti, ulsa=ulsa, statusi=False, cordinata=str1)
                insert1.save()

        reshtat = ['A','B','C']
        regjioni = Regjionet.objects.filter(emri="J105")[0]
        for resht in reshtat:
            reshti = Reshtat.objects.filter(emri=resht)[0]
            insert1 = Cmimet(regjioni=regjioni, reshti=reshti, cmimi=1)
            insert1.save()
        for resht in reshtat:
            for ulsa in range(1, 22):
                myArray = [d for i,d in enumerate(cordinates) if 'J105' in d['regionId'] and resht in d['rowID'] and d['sitId'] == ulsa]
                try:
                    str1 = ''.join(str(myArray[0]['cords']))
                except:
                    str1 = ""
                reshti = Reshtat.objects.filter(emri=resht)[0]
                insert1 = Ulset(regjioni=regjioni, reshti=reshti, ulsa=ulsa, statusi=False, cordinata=str1)
                insert1.save()

        reshtat = ['A','B','C']
        regjioni = Regjionet.objects.filter(emri="J106")[0]
        for resht in reshtat:
            reshti = Reshtat.objects.filter(emri=resht)[0]
            insert1 = Cmimet(regjioni=regjioni, reshti=reshti, cmimi=1)
            insert1.save()
        for resht in reshtat:
            for ulsa in range(1, 20):
                myArray = [d for i,d in enumerate(cordinates) if 'J106' in d['regionId'] and resht in d['rowID'] and d['sitId'] == ulsa]
                try:
                    str1 = ''.join(str(myArray[0]['cords']))
                except:
                    str1 = ""
                reshti = Reshtat.objects.filter(emri=resht)[0]
                insert1 = Ulset(regjioni=regjioni, reshti=reshti, ulsa=ulsa, statusi=False, cordinata=str1)
                insert1.save()

        reshtat = ['A','B','C']
        regjioni = Regjionet.objects.filter(emri="J107")[0]
        for resht in reshtat:
            reshti = Reshtat.objects.filter(emri=resht)[0]
            insert1 = Cmimet(regjioni=regjioni, reshti=reshti, cmimi=1)
            insert1.save()
        for resht in reshtat:
            for ulsa in range(1, 20):
                myArray = [d for i,d in enumerate(cordinates) if 'J107' in d['regionId'] and resht in d['rowID'] and d['sitId'] == ulsa]
                try:
                    str1 = ''.join(str(myArray[0]['cords']))
                except:
                    str1 = ""
                reshti = Reshtat.objects.filter(emri=resht)[0]
                insert1 = Ulset(regjioni=regjioni, reshti=reshti, ulsa=ulsa, statusi=False, cordinata=str1)
                insert1.save()


        reshtat = ['A','B','C','D','E','F','G','H','I']
        regjioni = Regjionet.objects.filter(emri="J108")[0]
        for resht in reshtat:
            reshti = Reshtat.objects.filter(emri=resht)[0]
            insert1 = Cmimet(regjioni=regjioni, reshti=reshti, cmimi=1)
            insert1.save()
        for resht in reshtat:
            for ulsa in range(1, 9):
                myArray = [d for i,d in enumerate(cordinates) if 'J108' in d['regionId'] and resht in d['rowID'] and d['sitId'] == ulsa]

                
                try:
                    str1 = ''.join(str(myArray[0]['cords']))
                except:
                    str1 = ""
                reshti = Reshtat.objects.filter(emri=resht)[0]
                insert1 = Ulset(regjioni=regjioni, reshti=reshti, ulsa=ulsa, statusi=False, cordinata=str1)
                insert1.save()



        reshtat = ['A']
        regjioni = Regjionet.objects.filter(emri="VIP1")[0]
        for resht in reshtat:
            reshti = Reshtat.objects.filter(emri=resht)[0]
            insert1 = Cmimet(regjioni=regjioni, reshti=reshti, cmimi=1)
            insert1.save()
        for resht in reshtat:
            for ulsa in range(0, 1):
                myArray = [d for i,d in enumerate(cordinates) if 'VIP1' in d['regionId'] and resht in d['rowID'] and d['sitId'] == ulsa]

                
                try:
                    str1 = ''.join(str(myArray[0]['cords']))
                except:
                    str1 = ""
                reshti = Reshtat.objects.filter(emri=resht)[0]
                insert1 = Ulset(regjioni=regjioni, reshti=reshti, ulsa=ulsa, statusi=False, cordinata=str1)
                insert1.save()
        
        reshtat = ['A']
        regjioni = Regjionet.objects.filter(emri="VIP2")[0]
        for resht in reshtat:
            reshti = Reshtat.objects.filter(emri=resht)[0]
            insert1 = Cmimet(regjioni=regjioni, reshti=reshti, cmimi=1)
            insert1.save()
        for resht in reshtat:
            for ulsa in range(0, 1):
                myArray = [d for i,d in enumerate(cordinates) if 'VIP2' in d['regionId'] and resht in d['rowID'] and d['sitId'] == ulsa]

                
                try:
                    str1 = ''.join(str(myArray[0]['cords']))
                except:
                    str1 = ""
                reshti = Reshtat.objects.filter(emri=resht)[0]
                insert1 = Ulset(regjioni=regjioni, reshti=reshti, ulsa=ulsa, statusi=False, cordinata=str1)
                insert1.save()

        reshtat = ['A']
        regjioni = Regjionet.objects.filter(emri="VIP3")[0]
        for resht in reshtat:
            reshti = Reshtat.objects.filter(emri=resht)[0]
            insert1 = Cmimet(regjioni=regjioni, reshti=reshti, cmimi=1)
            insert1.save()
        for resht in reshtat:
            for ulsa in range(0, 1):
                myArray = [d for i,d in enumerate(cordinates) if 'VIP3' in d['regionId'] and resht in d['rowID'] and d['sitId'] == ulsa]

                
                try:
                    str1 = ''.join(str(myArray[0]['cords']))
                except:
                    str1 = ""
                reshti = Reshtat.objects.filter(emri=resht)[0]
                insert1 = Ulset(regjioni=regjioni, reshti=reshti, ulsa=ulsa, statusi=False, cordinata=str1)
                insert1.save()

        reshtat = ['A']
        regjioni = Regjionet.objects.filter(emri="VIP4")[0]
        for resht in reshtat:
            reshti = Reshtat.objects.filter(emri=resht)[0]
            insert1 = Cmimet(regjioni=regjioni, reshti=reshti, cmimi=1)
            insert1.save()
        for resht in reshtat:
            for ulsa in range(0, 1):
                myArray = [d for i,d in enumerate(cordinates) if 'VIP4' in d['regionId'] and resht in d['rowID'] and d['sitId'] == ulsa]

                
                try:
                    str1 = ''.join(str(myArray[0]['cords']))
                except:
                    str1 = ""
                reshti = Reshtat.objects.filter(emri=resht)[0]
                insert1 = Ulset(regjioni=regjioni, reshti=reshti, ulsa=ulsa, statusi=False, cordinata=str1)
                insert1.save()

        reshtat = ['A']
        regjioni = Regjionet.objects.filter(emri="KMB")[0]
        for resht in reshtat:
            reshti = Reshtat.objects.filter(emri=resht)[0]
            insert1 = Cmimet(regjioni=regjioni, reshti=reshti, cmimi=1)
            insert1.save()
        for resht in reshtat:
            for ulsa in range(0, 1):
                myArray = [d for i,d in enumerate(cordinates) if 'KMB' in d['regionId'] and resht in d['rowID'] and d['sitId'] == ulsa]

                
                try:
                    str1 = ''.join(str(myArray[0]['cords']))
                except:
                    str1 = ""
                reshti = Reshtat.objects.filter(emri=resht)[0]
                insert1 = Ulset(regjioni=regjioni, reshti=reshti, ulsa=ulsa, statusi=False, cordinata=str1)
                insert1.save()

        

        