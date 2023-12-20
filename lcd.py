from datetime import datetime
class LCD:

    @classmethod
    def send(self,pack):
        f = open("/dev/lcpd", "w")
        f.write(pack)
        f.close()

    def text(self,txt):
        self.send(str(txt))


    def reset(self):
        self.send("\x1f")

    def timer(self):
        self.send("\x1b\x1a00\x3a00")

    def current_time(self):
        now = datetime.now()
        hour = now.strftime("%I")
        minutes = now.strftime("%M")
        self.send("\x1b\x1a"+ hour +"\x3a"+ minutes)


    def scroll(self,text,l=1,d=0):
        if not d == 0:
            if not l == 0:
                self.send("\x05"+text+"\x0d")
            else:
                self.send("\x1b\x06"+text+"\x0d")
        else:
            if not l == 0:
                self.send("\x1b\x0B"+text+"\x0d")
            else:
                self.send("\x1b\x07"+text+"\x0d")

    def cursor(self,sw=1):
        if sw == 0:
            self.send("\x14")
        else:
            self.send("\x13")


    def smart(self,msgs,d=0,l=0):
        first = 1
        if d == 0 and l == 0:
            packet = "\x1b\x15"
        if d == 1 and l == 0:
            packet = "\x1b\x16"
        if d == 0 and l == 1:
            packet = "\x1b\x13"
        if d == 1 and l == 1:
            packet = "\x1b\x14"

        for msg in msgs:
            if not first == 1:
                packet = packet + "\x1c"
            first = 0
            packet = packet + msg
        packet = packet + "\x0d"

        self.send(packet)

   #def brightness()


    def digit_select(self,digit = 0):
        packet = "" + hex(digit)
        self.send(packet)
