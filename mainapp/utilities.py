from PIL import Image,ImageDraw,ImageFont
from num2words import num2words
from .models import Room,Count

def dateformat(date):
    date = str(date).split("-")
    return "{}/{}/{}".format(date[2],date[1],date[0])


def gen_duesbill(request):
    name = request.POST.get("name")
    room = request.POST.get("room")
    date = request.POST.get("date")
    fdate = request.POST.get("fdate")
    tdate = request.POST.get("tdate")
    total = request.POST.get("total","00")
    adv = request.POST.get("adv","00")
    due = str(int(total)-int(adv))
    

    with Image.open("duesbill.jpg") as im:
        draw = ImageDraw.Draw(im)
        font = ImageFont.truetype("robold.ttf",size=26)
        draw.text((233,411),name,fill="rgb(0,0,0)",font=font)
        draw.text((268,448),room,fill="rgb(0,0,0)",font=font)
        draw.text((765,411),dateformat(date),fill="rgb(0,0,0)",font=font)
        draw.text((1300,411),dateformat(fdate),fill="rgb(0,0,0)",font=font)
        draw.text((1260,448),dateformat(tdate),fill="rgb(0,0,0)",font=font)
        draw.text((1298,582),total,fill="rgb(0,0,0)",font=font)
        draw.text((1298,752),adv,fill="rgb(0,0,0)",font=font)
        draw.text((1298,807),due,fill="rgb(0,0,0)",font=font)
        im.save("mainapp/static/duebill.jpeg")

def gen_moneyreciept(request):
    count = Count.objects.first()
    name = request.POST.get("name","xyz123")
    amount = request.POST.get("amount","00")
    room = request.POST.get("room","000")
    recieptno = str(count.value+1)
    date = request.POST.get("date")
        
    with Image.open("moneyreciept.jpg") as im:
        draw = ImageDraw.Draw(im)
        font = ImageFont.truetype("robold.ttf",size=36)
        draw.text((759,457),name,fill="rgb(0,0,0)",font=font)
        draw.text((523,527),amount+"/-",fill="rgb(0,0,0)",font=font)
        draw.text((1439,336),room,fill="rgb(0,0,0)",font=font)
        draw.text((1369,280),date,fill="rgb(0,0,0)",font=font)
        draw.text((356,284),recieptno,fill="rgb(0,0,0)",font=font)
        draw.text((455,745),num2words(int(amount)) + " only",fill="rgb(0,0,0)",font=font)
        im.save("mainapp/static/moneyreciept.jpeg")
    count.value = count.value + 1
    count.save()


def gen_inv(o,copy='cc'):
    desc = Room.objects.get(room_no=o.room_no).description
    try: desc2 = Room.objects.get(room_no=o.room_no_2).description
    except: desc2 = ""
    try: desc3 = Room.objects.get(room_no=o.room_no_3).description
    except: desc3 = ""

    if copy=='cc':
        ip = 'TIV(CC).jpg'
        op = 'mainapp/static/invcc.jpeg'
    else:
        ip = 'TIV(HC).jpg'
        op = 'mainapp/static/invhc.jpeg'
 
    with Image.open(ip) as im:
        draw = ImageDraw.Draw(im)
        font = ImageFont.truetype("robold.ttf",size=28)
        draw.text((158,386),str(o.name),fill="rgb(0,0,0)",font=font)
        draw.text((219,421),str(o.phone),fill="rgb(0,0,0)",font=font)
        draw.text((187,460),str(o.address),fill="rgb(0,0,0)",font=font)
        draw.text((221,325),str(o.invoice_no),fill="rgb(0,0,0)",font=font)
        draw.text((1290,316),dateformat(o.date.isoformat()),fill="rgb(0,0,0)",font=font)
        draw.text((1080,376),o.company_name if o.company_name else "",fill="rgb(0,0,0)",font=font)
        draw.text((1000,415),o.gstin if o.gstin else "",fill="rgb(0,0,0)",font=font)
        #room_1
        draw.text((60,562),o.room_no,fill="rgb(0,0,0)",font=font)
        font = ImageFont.truetype("robold.ttf",size=26)
        draw.text((221,562),desc,fill="rgb(0,0,0)",font=font)
        font = ImageFont.truetype("robold.ttf",size=28)
        draw.text((560,562),dateformat(o.check_in.isoformat()),fill="rgb(0,0,0)",font=font)
        draw.text((732,562),dateformat(o.check_out.isoformat()),fill="rgb(0,0,0)",font=font)
        draw.text((916,562),str(o.days_count),fill="rgb(0,0,0)",font=font)
        draw.text((1080,562),str(o.rate/1),fill="rgb(0,0,0)",font=font)
        draw.text((1280,562),str(o.total()/1),fill="rgb(0,0,0)",font=font)
        #room_2
        if o.room_no_2:
            draw.text((60,612),o.room_no_2,fill="rgb(0,0,0)",font=font)
            font = ImageFont.truetype("robold.ttf",size=26)
            draw.text((221,612),desc2,fill="rgb(0,0,0)",font=font)
            font = ImageFont.truetype("robold.ttf",size=28)
            draw.text((560,612),dateformat(o.check_in_2.isoformat()),fill="rgb(0,0,0)",font=font)
            draw.text((732,612),dateformat(o.check_out_2.isoformat()),fill="rgb(0,0,0)",font=font)
            draw.text((916,612),str(o.days_count_2),fill="rgb(0,0,0)",font=font)
            draw.text((1080,612),str(o.rate_2/1),fill="rgb(0,0,0)",font=font)
            draw.text((1280,612),str(o.total_2()/1),fill="rgb(0,0,0)",font=font)
        #room_3
        if o.room_no_3:
            draw.text((60,662),o.room_no_3,fill="rgb(0,0,0)",font=font)
            font = ImageFont.truetype("robold.ttf",size=26)
            draw.text((221,662),desc3,fill="rgb(0,0,0)",font=font)
            font = ImageFont.truetype("robold.ttf",size=28)
            draw.text((560,662),dateformat(o.check_in_3.isoformat()),fill="rgb(0,0,0)",font=font)
            draw.text((732,662),dateformat(o.check_out_3.isoformat()),fill="rgb(0,0,0)",font=font)
            draw.text((916,662),str(o.days_count_3),fill="rgb(0,0,0)",font=font)
            draw.text((1080,662),str(o.rate_3/1),fill="rgb(0,0,0)",font=font)
            draw.text((1280,662),str(o.total_3()/1),fill="rgb(0,0,0)",font=font)

        draw.text((1280,759),str((o.total()+o.total_2()+o.total_3())/1),fill="rgb(0,0,0)",font=font)
        draw.text((1280,797),str(o.gst()),fill="rgb(0,0,0)",font=font)
        draw.text((1280,834),str(o.gst()),fill="rgb(0,0,0)",font=font)
        draw.text((1280,870),str(o.total_with_gst()),fill="rgb(0,0,0)",font=font)

        draw.text((184,759),str(o.check_in),fill="rgb(0,0,0)",font=font)
        draw.text((661,759),str(o.final_checkout()),fill="rgb(0,0,0)",font=font)
        draw.text((1122,921),str(o.remark),fill="rgb(0,0,0)",font=font)
        im.save(op)

