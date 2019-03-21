from PIL import Image,ImageDraw,ImageFont
from num2words import num2words
from .models import Room

def dateformat(date):
    date = str(date).split("-")
    print(date)
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
    name = request.POST.get("name","xyz123")
    amount = request.POST.get("amount","00")
    room = request.POST.get("room","000")
    recieptno = request.POST.get("recieptno","000")
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


def gen_inv(o,copy='cc'):
    desc = Room.objects.get(room_no=o.room_no).description
    if copy=='cc':
        ip = 'TIV(CC).jpg'
        op = 'mainapp/static/invcc.jpeg'
    else:
        ip = 'TIV(HC).jpg'
        op = 'mainapp/static/invhc.jpeg'
 
    with Image.open(ip) as im:
        draw = ImageDraw.Draw(im)
        font = ImageFont.truetype("robold.ttf",size=28)
        draw.text((158,386),o.name,fill="rgb(0,0,0)",font=font)
        draw.text((219,421),o.phone,fill="rgb(0,0,0)",font=font)
        draw.text((187,460),o.address,fill="rgb(0,0,0)",font=font)
        draw.text((221,327),str(o.invoice_no),fill="rgb(0,0,0)",font=font)
        draw.text((1290,316),dateformat(o.date.isoformat()),fill="rgb(0,0,0)",font=font)
        draw.text((1080,376),o.company_name,fill="rgb(0,0,0)",font=font)
        draw.text((1000,414),o.gstin if o.gstin else "",fill="rgb(0,0,0)",font=font)
        draw.text((60,562),o.room_no,fill="rgb(0,0,0)",font=font)
        font = ImageFont.truetype("robold.ttf",size=26)
        draw.text((221,562),desc,fill="rgb(0,0,0)",font=font)
        font = ImageFont.truetype("robold.ttf",size=28)
        draw.text((566,562),dateformat(o.check_in.isoformat()),fill="rgb(0,0,0)",font=font)
        draw.text((737,562),dateformat(o.check_out.isoformat()),fill="rgb(0,0,0)",font=font)
        draw.text((916,562),str(o.days_count),fill="rgb(0,0,0)",font=font)
        draw.text((1080,562),str(o.rate/1),fill="rgb(0,0,0)",font=font)
        draw.text((1280,562),str(o.total()/1),fill="rgb(0,0,0)",font=font)
        draw.text((1280,759),str(o.total()/1),fill="rgb(0,0,0)",font=font)
        draw.text((1280,797),str(o.gst()),fill="rgb(0,0,0)",font=font)
        draw.text((1280,835),str(o.gst()),fill="rgb(0,0,0)",font=font)
        draw.text((1280,870),str(o.total()+o.gst()*2),fill="rgb(0,0,0)",font=font)
        im.save(op)

