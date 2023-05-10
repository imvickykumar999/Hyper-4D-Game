
># `Join World`
>
>![image](https://user-images.githubusercontent.com/50515418/235355886-1990a4ef-65a6-4a42-92d8-e649d2d7251a.png)

<br>

`Continue World` :

        python minecraft.py home night

`New World` :

        python reset.py new
        
`On Reset` : 

        {"position": []}
        
------------------------

`Arguments` **are** `world` *and* `sky` :

        try:
                data = sys.argv[1]
        except:
                data = 'home'

        try:
                sky = sys.argv[2]
        except:
                sky = 'night'


