summary of last lecture 
lets quickyunderstand the genric flow , request will go to lb which will redirect to application servers then application servers they might  need some data for which they will reach out to db servers, so this databse call might be very heavy we might fetch a lot of data its possible that we r fetching the dsame data againa nd again so thats y we can implement a layer of caching in betwerm , app servers will ask the cache if the value is there in cache then in that case it will return directly , however if the value is not presnt there in that case the app servers will reach out to the db     
now sql queries is goign to execute and is going to fetch the data that was required there , ythis is a v ery basic read query ,
<img width="431" height="168" alt="image" src="https://github.com/user-attachments/assets/66a4b123-0d2d-46e4-ad38-6239f30f13b3" />  

in an async way the value will also get yupdated inside the cache 
  
lets see how write executs so a = 10 is presentin cache amnd databse update a = 100 request comes now 
<img width="440" height="186" alt="image" src="https://github.com/user-attachments/assets/62287c21-cf60-4eeb-b56a-df2a4549c4a7" /> 
so here app servers is directly goinf to go to the db servers and dfb will return some status code to ensure that yhe app servers gets some acknowledgement that the value is updaeted 
once it is acknowledgement the same is sent to the user 
this is why we need cache invalidation strategy 

ttl -> data in cache will have some expiry date whenever a read request comes it checks the expiry date , if the date is passed then it is a cache miss in that case it willreach the db servers get the correct value and then in an async way also update the cache but the stale value can be deleted from the cache  should we do this division in a proacticve way  should we run a script that checaks all the entries  which are present inside the ache cheks their expiry date , no right that is an extra work , when we r reading the data at time do the validation however in some cases deppending on the scenario  we might run a seperate script as well which will run lets say once everyday , or 15 days 
<img width="445" height="228" alt="image" src="https://github.com/user-attachments/assets/24f7698a-1dcd-4c1e-af18-61e927c34be6" /> 

what types of consistebcy does ttl provides us -> does it provides us immediate consistency , no it provides us eventual consistency whatver is the ttll whatver is the expiry date till that point we will keep certain expired data nd in tat certain use case we should be ok with it , only then we r goign to use it , if wer not ok with it we r not going to use it so it our choice 
which invalidation strategy provides us immediately consistency not eventual consistency -> write through what is going to happen in write through it meansall of the write ipeartions should be done in both te places write request goes to the db which sends some acknowledgement  ,if it a successthen we r at the same time also goignt o make an update in the cache however if thsi acknowledgement is not sucees then we wont update the cache what we want here is knows as two faced commit 
we r commiting same value at 2 different places this is very similar to maintaining consistency in case of database transactions 
<img width="583" height="296" alt="image" src="https://github.com/user-attachments/assets/0fb7aaf4-c6d2-4fac-9e74-71c69c6e2fc4" /> 

in db trandaction lets say we have account a and account bboth have 1000 , i wan tot reduce 500 from firsta nd add i  second 
ence here 4 different quesries are goignt o run if anyof them fails , then overall state of the data becomes inconsistent , we solved  this usi gtransactions which are supposed to be atomic innature , if one of the transaction fails it will result in the failure of all of them 
sio similarly if ive updated in my databse and thne the cache updation fails then tht is a prblm and th emore network qureries wehave the more complexity we r goign to create 
so we need to retrying and there will be multiples astartegy for tat 
b ut hte only way to solve this is retry and the end user will wait for acknowledgement 
write through is going to provide u immediate consistency but it comes with its own complexities implementing writye through in a distributed system where  u have multipel servers where u have replica of every servers which means that we have to mak ethe same update in ram bcoz all replicas are goign to have the same data some of them r goign to be copies of these 
in this same write through if we shift from global cache ot local cache then it becomes eay 
do u know y ? what is a local cache we wont have this cace implemented in a different server , cache will be a part of application server, so this is no external server , the ram of the paplicatoion serverwill be used , but it is not necessary that the ca he will always be a ram 
also in egenral it is a key value pair but the cache is not supposed to e a key value value always , <img width="463" height="203" alt="image" src="https://github.com/user-attachments/assets/9bb08bd2-980e-45f5-8e15-df20964868ec" />
now in this case if u want ot implement a two facesd commit  which means u need to update this value inside the db server we also wantto update this in the cache hence this iwll be more easy and this wont fail but there is a condition here ot achive this
so a gets upsdated to 100 in db servers also in the first application server however if the same variable is present in other servers then it is almost impossible 
so fro this to happen these app servers must be stateful 

then there was another policy called write around 
lets conider a scenario , u want to store some data but gettingthat data is the harder part , for eg the match win percemtage scenaroio there are goignt o be multiple tables and we will write so many queries , if we r using ttl im thatcase , the moemnt ttl expires all of the application servers  will reach out to the databse for that specific data so we r going to get so many complicated  queries of all the applicatikon servers, whatveer fdata we wnat we wills tore it in cache and we r goignt o run scripts or projobs ata  fixed interval of timethat projob is goign to fetch the data once for all the servers , servers are not going to requets the data from the db ,
servers will chcek in the cache and return it 
eg -> m1 vs rcb win percentgae is stored -> after a while we need to update this again so instead of storing a ttl of 30 misn, which will push these application servers to reach out to the db , what we will do is after 30 mins we will  run a script this script fetched teh data does the calculation and updates the value directly ehre , application servers will never be updating the cache , <img width="584" height="350" alt="image" src="https://github.com/user-attachments/assets/c196d968-69bb-4270-9f93-60bf24e0bc54" />

now we haave anote rpolicy called write back -> we do the write and update in the cache not in the db when do u think we should be suing this approach , when we r ok losimg some anmount of data bcoz if wer  keeping the data inside the cache , we get a write request , we update it directly in the cache and after a while we copy it in the db as well , the moment power goes down or the server crashed , then the data is lost 
for maintaining youutbe video views ,the views of live users ,no of likes in a reel which was gone viral these type of datapoints can be stored ina write back cache , we keep updtaing in cache so that we avoid doing thatin db when we have a bunch of updates then we run a script wcih copies this data int he db 

quiz 1 
Which consistency model does TTL-based invalidation generally provide?
Eventual consistency

What is the main trade-off when choosing a very low TTL?
Fresher data but more cache misses

so if ur setting a very small ttl what does it mean that the data will expire very quickly , means if my data is updated  frequently then chances of getting the newest data is very high however we iwll also be having  a lot of cache misses bczo everytime we fetch teh data we may see thatthe expiry date has expired , so we will have ot fech it from the db ,

In lazy invalidation, when is an expired cache entry usually deleted?
When the next read request for that key comes

so by lazy invalidation we mean that we r not doing that running scrupt and checking i df the expiry date has passed lazy means when we fetch teh data at that time we check what si teh expiry date whta is the current date based on that we make a decision of deleting the data or invalidating the data 

Write Around caching is most suitable when:
Data fetching or computation from the database is expensive.

bcoz we dont want many requets to hit on the databse at the sma etime 

Why is Write Through difficult in distributed systems?
Because ensuring atomic writes across cache and database is hard.

here we r tinkign of it as one server but in relaiyt htose data are replicated 

there was a questionw hcih we left unsolved in the prvious class 
whenever we submit our code it is executed against a fixed set of tests cases those test cases are stored in a a file , file wont be stored in a sql db bcoz sql is not made for storing large files , file willl be stgored ina  diff db like file storage servive so downloading the file every single time whenever  u have to evaluate the code that is goign to be a very time taking operation  which will increa e the latency so how iwll we reduce the latency 
the ans is simple we have to cach ethe data  buit this shoudlnt be an interview ans we need to talk about the invalidation , how r we goint o creaet space in te achhe ,eviction policy , r u goign with distributed cache or single server cache , do u want a global caxce o r a local cache if it is a distributed cache then how exactly load balancing is goign to work in taht case 
therree is a 5 step process ot oslve this 
at first u wont be directly aksed to implement the cache we will always be solving a bigger problem , the respnse time of the api is too much 
then we iwll have to decide whether wehave to go ahead with other difoptimimzations or whether we should be miplementing a cache , bcoz cache comes with its own advnatages and disadvantages which increases overall complexity fo yhe syystem , firts we need to justify the need of cache 
then think type o fcaching , global or local , global in single or distributed then the eviction algorithm 
<img width="385" height="104" alt="image" src="https://github.com/user-attachments/assets/b814666a-6ba1-4e7e-a0bd-e842f1858754" />
99 percent we will use lru eveiction 
then cache invalidation like write through write back , we can amke a combination of these or seperate 
the question whihc iw eneed to think about is that what type of consistency do we need in out system do we nee dimmediate consistency , do we want eventual consistency or having no consistency at all is also going to be ok with respect to my specific use case depending on these answers im going to choose my invalidation strategy 
once u have answered lal of these then ur goign to the last thing if it is distributed cache or not , mutiple servers here means lb so wht type of algorithm should we be running , should all those servers be stateful statelessshould it be round robin or consistent hashing that we will decid ein the 
so in acse of scaler do u think that we need cache , do u think a cache is goint ot optimize the latency for the user , the user hits api presses submiy t button , the user id is sent in the api , then the problem id an dthen  the caode and then some meta data about the code then lb redirects it to osmeof the app servers and this needs to know if the user is even authorized ot solve the problem 
then the app server also thinks what is time and space complexity of the prblm , only then when it executes it decided what it should be for this it needs to query the databse inside the db tehre must aeb a table which has prblm id , time complexity , space complexitya nd exact time of execution exact memeory and thsi will store url of test cases and output url also 
an entire row will be fetched by app servers and all of this data 
then this application servers will recah out to th es3 servers and then they will upload these large files , 
how large tehse files wwill eb <img width="558" height="360" alt="image" src="https://github.com/user-attachments/assets/003c0afb-69e6-40eb-8373-6e1291c2a88d" />
or can u esitmiatethe size withotu even looking at the file size , we will aprox 
time limit -> 100 to 1000 max test cases 
eg -> sort an array , what is the max size of an array , approx 10 to the power 6 in c++ usingglobal array it can be 10 to the o=power 7 
what is the size of 1 file -> 100 arrays * 10^6 * 8byte integer size = 800mb
<img width="432" height="271" alt="image" src="https://github.com/user-attachments/assets/bf584a8e-7d8e-42d3-8e99-bb35710a855e" />
we will take approx 1 gb 
we will download 1 file for time limit , amother for memory limit 1 outpur file for time limit ,1 fiel for memory output 
so we have 4 such files which needs to be downloaded 
so we need to download 4 gb data , when 
so generally if all of this is parrt  of aws s3and the server will be connected with a very high speed
internet file if they r connected with very high speed file the speed would be somewhere around 10 gbps , it is bits per second not bytes , it appears to be lafge but it is small 
so 4 bytes has 32 bits , so we need around more than 3 secs to download this data this is when the connection between application servers and s3 is seamless
<img width="587" height="393" alt="image" src="https://github.com/user-attachments/assets/b0527696-ba89-49e9-8070-5ad87d6bf49e" />
do we need cache 
we can cancel thsi download if we store this data somewherein the cache so now we have an objective evaluation if we need teh cache or not , now what type of cache do we want do we wnat global cach e or local caceh
how do we decide if we need global or local cache 
if the same dtaa is replicated or all application servers if we dont want different data for diff sevrs which means our servers are staeless we can go ahead with global cacge 
same ytest case data hence we will go ahegd with gloval cache <img width="539" height="287" alt="image" src="https://github.com/user-attachments/assets/bca7d9c6-38d3-4afa-a649-a9db2e887ab8" />
we added a cache -> requets come to application servers , it reaches ou tto databse servers and it checks for all metadata for teh problem , as of now all the calculations which we have done were to justify all teh files we r still goign to fetch all the met adata form teh sql , based on the metadata now weknwo what is the url of the test case files , we will check in teh cache , if it is present we will downlaod from cache , same anmount of adta and same time and same speed so cache is noit reducing latency , so if same data is required by all teh servers global case will eb teh answer nbut not in this case 
so we will see local cage now 
so request goes form application servers to db and then it returns then teh application server itself is checked if it not tehre teh jn it goes to s3 
once this data is downloaded next time itr will check its own memory 
now how many sych files wil be tehre 
fir one prblm files wil lbe updates at max once per year 

peter norwixk -> there r o nly 2 things that hard in cse , namin the vairables and cache invalidation 
 <img width="505" height="313" alt="image" src="https://github.com/user-attachments/assets/8015426e-2e28-46da-9952-3109a954ab3f" />
eventual consistency means thta the test cases are wrong , thye have been updated in teh actual fiels 
but if it havent been loaded inteh cache the u wont getteh updated test cases 
here we wnat immediate consistency how do we gettaht -:> write through cache , how to implement as this is hard in global cache , 
if ur having a 5 giga hertz wht does it mean , 5 ghz means it will hve 5 * 10 ^9 clockticks per sec 
<img width="593" height="358" alt="image" src="https://github.com/user-attachments/assets/ee9b26de-e8da-47d2-bd73-f2d009708ff5" />
<img width="558" height="368" alt="image" src="https://github.com/user-attachments/assets/f7818571-2f8c-4403-8fdb-5fabecd8205d" />
like htis calculation we can do more 5 * 10 ^ 9 in 1 sec
<img width="490" height="181" alt="image" src="https://github.com/user-attachments/assets/d02b2d76-61af-46fb-a374-5a91eea8fbd1" />
the cpu will eb having 4 cores 
in 0.2 nano seconds it can take 4 such calculations 
the amount of time it atkes 1 photon to recahmmy eyes frm my laptop 25 cm away is the same the cpu can do 20 calcultion s
so cpu is never teh bottleneck the bottlenecki smemory os that we have layers of emory 
scheduling algorithms help us utilise the cpu in teh best possible wya 
but this happens for i/o bound processes , some processes are also cpu bound whchwill  not leav ethe cpu fro eg the ports that ur goignt o execute 
we make the use of cpu by using multi threading  
some poroceeses are also cpu bound which wont leave the cpu for eg teh ports that ur goignt o execute these ports are nto i/o bound the entiree dtaathat u need to run is already there all the data strcutrures all are already tehr ein teh cache so these proceessa re cpu bound whichmena s at a time how many codes a cpu can run if it is a 4 core cpu , its goignt o run 4 codes ta a time , 1 code will take 3 - 5 secs , eays will atke 1 sec 
we cannot have all the problems hitting at one server , we will ahve to distribute tehm these servers should have stateless 
now implementation of write through is easier or hard , it is hard , now we need togog to lla of the servers and run the update script which is harder so how do we solve this now 
when do we need consistency -> suppose im caching aadhar card no will there be a case ive to update aadhar case this wont have it wont get invalid , if teh data is immutablewe wont have to worry about immutabloe 
so what if we make these files immutable -> we can make teh file consistent but we will change teh name of the file so taht we enevr stale dat a
we have a file testcasev1txt , it is stored in accahe and s3 server when we have an update we change the file name in s3 <img width="651" height="378" alt="image" src="https://github.com/user-attachments/assets/f7dde584-b662-4b9d-a815-6723082e9e72" />

so when dta ais not present in cache asthe file name changed tehn we nee dto download teh data fomr s3 
<img width="627" height="361" alt="image" src="https://github.com/user-attachments/assets/b6b75ac2-5558-46ef-a5d0-f1e7e45300f0" />
ive a prblm id 20 which has a file testcasev1.txt so a request comes we r goign to go to the databse inside thisd aatbase for teh prblm statement u will see that the url has testcase1.txt , fetches the meta data gets to know teh name of the fiekl is this seraches , now the update request makes changes and now we cnage teh name of the fiel and it updateds the database so we wont find this foile no w
in scaler we don not version the files using a number we use the exact timestamp wjere the file is recreated first that name ui sdownlaodedf rom teh sql 
we dont use cdn bcoz usme we set the data , 



problem ststement 
we need to design that leaderboard -> we have username , marks in every question , no of attemps tand time and then we have score and then we will ahve rank , we also have pagnation <img width="579" height="321" alt="image" src="https://github.com/user-attachments/assets/f1c16fd1-1325-4caa-902e-fd3ba3b14dbf" />
so they provide us my rank is every page so taht we dont ahve to find it , do we need a cache
we need to come up with some numbers to answer thsi 

in sql there is a user table , problem table , constest data table , relation of problem contest table , 
<img width="882" height="462" alt="image" src="https://github.com/user-attachments/assets/6be92b56-e3a0-45a2-9af9-6fdf4c02ada0" />
we will use multiple joins , group by , offset , 
<img width="535" height="180" alt="image" src="https://github.com/user-attachments/assets/ebf3500c-5df1-4af8-ae79-436ed7e14582" />
so every sec the keaderboard can change 50 times 
we definitely need a cache 
