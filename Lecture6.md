<img width="535" height="374" alt="image" src="https://github.com/user-attachments/assets/e1a8ff85-5155-4b05-b09e-80cd5bd8a77d" /> 
<img width="245" height="47" alt="image" src="https://github.com/user-attachments/assets/9a1235a4-3870-4019-81e5-faa26f0190fa" />   
this daata is small ,we get ram 8 gb ,   
<img width="471" height="256" alt="image" src="https://github.com/user-attachments/assets/423bf103-38ea-44f7-8f8a-c53c7d02f191" />    
on an average every user will see leaderboard every 10 mins    
<img width="439" height="179" alt="image" src="https://github.com/user-attachments/assets/459b58af-f3eb-42a3-ae03-d4ef91646788" />    
this is y we  will implement cache here but whttio implement     
so should we go ahed with distributed cache or a single cache y single , the data is same size is small 
we will be using distributed cache when we have a lot of data and that data doesnt fit in the ram of one server this time it is supposed ot be the ram nto the hard dsisk     
so global cache and single server    
now what is the invalidation mechanism -> immediate consistency cant be provdie leaderbaord cany change every second  
should we use writeback , what is a writeback cache  -> we update inthe cache and then we run a job which fills the data in th databse but this wont work here 
so which cache iwll be usedhere , we can keep a ttl or 5 or 10 mins,in majority of teh cases we r goign to use ttl asthe invalidation policy    
we can use ok 
what shoudl be ttl what time -> 20 mins 
<img width="479" height="199" alt="image" src="https://github.com/user-attachments/assets/7b1408b2-acb5-48e9-9fbd-61722add15de" />

what if the ttl expires here , it will reach out to the daytabase but we hve 100 thousand of uses , if cache expires everyone will go to databasr , 
so ere ttl shoulf not be used we should use write around -?> 

write around means there wont be any ttl -> it wont have ttl it runs for any time intervala nd it simpley updates teh leaderboard in the cach e, application servers are not going to reach out to the databse 
now what type of load baalncer do we nee d-> round robin or consistent hashing  , we have a single server so we dont need b , lb will  only be required if we have distributed  cache

what about teh eviction  policy ->lru , do we need eviction -> no we dont need but once the contest is over ,after that we acn simply erase loop from the cache coz we wont receive any submission after that so we can dump the daata after contest ends 
so now how do we store teh leaderboard data in teh cache , teh cache that we r going to use for thsi case which we use in scaler is key value based cache 

simialr to hashmap and we use software redis which provides us this and also it is widelt used 
key should be theuser 
for the last row the key has to be user 

<img width="641" height="346" alt="image" src="https://github.com/user-attachments/assets/c6f91a18-2fde-4472-8b16-0c61fc7e3f4f" />
caching has nothing to do with databas e indexing ,  

<img width="410" height="213" alt="image" src="https://github.com/user-attachments/assets/00bc8932-1041-47ea-923e-9264628b3533" />
<img width="412" height="216" alt="image" src="https://github.com/user-attachments/assets/92184634-d8c8-41fa-88ca-162d9a74f9a7" />
<img width="350" height="162" alt="image" src="https://github.com/user-attachments/assets/860bd8f0-5238-468c-a5ec-a8e757711031" />
<img width="427" height="182" alt="image" src="https://github.com/user-attachments/assets/93dedbdd-64b9-400e-a417-f5a01f5531e5" />


next case study 
design a social media profile page -> when we opem n out profile we see manyposts, in facebook u can a;lso post on yur frnds profile 
