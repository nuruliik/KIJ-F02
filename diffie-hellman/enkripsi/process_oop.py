import Konstanta
import binascii

class process_oop:

    loop = 0

    def permutation(self,pc_table,key_or_plaintext,type):
        if type == "string":
            afterPermut = ""
            for x in range(0,len(pc_table)):
                afterPermut+=key_or_plaintext[pc_table[x] - 1]
        elif type == "list":
            afterPermut = []
            for i in range(0, 15):
                temp = ""
                for j in range(0, len(pc_table)):
                    temp += (key_or_plaintext[i][pc_table[j] - 1])
                afterPermut.append(temp)
        else :
            afterPermut = ""
            for x in range(0, len(pc_table)):
                afterPermut += key_or_plaintext[pc_table[x]]
        return afterPermut

    def bin_to_hex(self,bit):
        hexstr = '%0*X' % ((len(bit) + 3) // 4, int(bit, 2))
        return hexstr

    def hex_to_bin(self,hexstr):
        return "{0:8b}".format(int(hexstr, 16))

    def shift(self,string,num):
        string_new = string[num:] + string[:num]
        return string_new

    def split(self,string,type):
        if type == "string":
            split_num = len(string) / 2
            str_1 = string[:split_num]
            str_2 = string[-split_num:]
        else :
            split_num = len(string)/2
            str_1 = [string[:split_num]]
            str_2 = [string[-split_num:]]
        return str_1,str_2

    def xor(self,num1, num2):
        result = ""
        for i in range(0,len(num1)):
            if bool(int(num1[i])) != bool(int(num2[i])):
                result += '1'
            else:
                result += '0'
        return result

    def initsbox(self,table):
        for i in range(0, 4):
            for j in range(0, 16):
                table.s1_table[i][j] = '{0:04b}'.format(table.s1_table[i][j])
                table.s2_table[i][j] = '{0:04b}'.format(table.s2_table[i][j])
                table.s3_table[i][j] = '{0:04b}'.format(table.s3_table[i][j])
                table.s4_table[i][j] = '{0:04b}'.format(table.s4_table[i][j])
                table.s5_table[i][j] = '{0:04b}'.format(table.s5_table[i][j])
                table.s6_table[i][j] = '{0:04b}'.format(table.s6_table[i][j])
                table.s7_table[i][j] = '{0:04b}'.format(table.s7_table[i][j])
                table.s8_table[i][j] = '{0:04b}'.format(table.s8_table[i][j])

    def sbox_transformation(self,sbox_key1,sbox_key2,table_key,e_message,object):
        if table_key== 0:
            table = object.s1_table
        elif table_key== 1:
            table = object.s2_table
        elif table_key== 2:
            table = object.s3_table
        elif table_key== 3:
            table = object.s4_table
        elif table_key== 4:
            table = object.s5_table
        elif table_key == 5:
            table = object.s6_table
        elif table_key == 6:
            table = object.s7_table
        else :
            table = object.s8_table

        bit1 = e_message[0]+e_message[5]
        bit2 = e_message[1:5]
        index_bit1 = sbox_key1.index(bit1)
        index_bit2 = sbox_key2.index(bit2)
        return table[index_bit1][index_bit2]

    def enkripsi(self,key,plaintext):
        #instance table
        table = Konstanta.Konstanta()

        #--------------get the key--------------------------#
        key_p_new = []
        # key_bit = "".join(format(ord(x), "08b") for x in key)
        key_bit = key
        key_p=self.permutation(table.pc1,key_bit,"initial")
        key_p1, key_p2 = self.split(key_p,"list")
        for i in range(0,16):
            key_p1.append(self.shift(key_p1[i],table.number_of_shift[i]))
            key_p2.append(self.shift(key_p2[i],table.number_of_shift[i]))
            key_p_new.append(key_p1[i] + key_p2[i])
        key_p_new_p =  self.permutation(table.pc2,key_p_new,"list")
        #---------------end of get the key------------------#

        #-----------------encrypt the message------------------#
        # message_bit = "".join(format(ord(x),"08b")for x in plaintext)
        message_bit = plaintext
        message_p = self.permutation(table.pc_messsage1,message_bit,"string")
        mes1,mes2 = self.split(message_p,"string")

        for i in range(1,len(key_p_new_p)):

            e_mes2 = self.permutation(table.e_table,mes2,"string")
            hasil_xor=""
            for j in range(0, len(e_mes2)):
                hasil_xor+=self.xor(key_p_new_p[i][j],e_mes2[j])

            s_mes2=""
            counter = 0
            for j in range(0,8):
                s_mes2+= self.sbox_transformation(table.s_box_key_1, table.s_box_key_2, j ,hasil_xor[counter:counter+6] , table)
                counter+=6

            p_mes2 = self.permutation(table.p_table,s_mes2,"string")
            for j in range(0,len(p_mes2)):
                mes2 += self.xor(mes1[j], p_mes2[j])
            mes1 = mes2

        reverse_connecting = mes2 + mes1
        chipertext = self.permutation(table.reverse_table,reverse_connecting,"string")

        return chipertext

    def ofb_enkripsi(self,plaintext,key):
        #instance tabel
        table = Konstanta.Konstanta
        if self.loop==0:
            self.initsbox(table)

        # konvert plaintext dan key
        plaintext_bit = ''.join(format(x, 'b').zfill(8) for x in bytearray(plaintext))
        key_bit = ''.join(format(x, 'b').zfill(8) for x in bytearray(key))

        #-------------------OFB ENKRIPSI------------------------------#
        text_length = len(plaintext)
        iv = table.iv
        count = 0
        chipertext_bit = ''
        while text_length > 0:
            #cek kekurangan bit
            if text_length < 8:
                p_text = plaintext_bit[count * 64:count * 64 + 8 * text_length]
                for i in range(0, 8 - text_length):
                    p_text = p_text + '00000000'
            else:
                p_text = plaintext_bit[count * 64:count * 64 + 64]
            #Enkripsi DES
            e_bit = self.enkripsi(iv, key_bit)

            iv = e_bit
            chipertext_bit += self.xor(p_text, e_bit)
            text_length -= 8
            count += 1
        self.loop+=1
        return self.bin_to_hex(chipertext_bit)

    def ofb_dekripsi(self,chipertext,key):
        #instance table
        table = Konstanta.Konstanta()
        if(self.loop==0):
            self.initsbox(table)

        #Konvert chipertext dan key
        chipertext_bit = self.hex_to_bin(chipertext)
        key_bit = ''.join(format(x, 'b').zfill(8) for x in bytearray(key))

        #-------------------OFB DEKRIPSI-------------------------#
        chipertext_length = len(chipertext) / 2
        iv = table.iv
        count = 0
        plaintext_bit = ''
        while chipertext_length > 0:

            #cek kekurangan  bit
            if (chipertext_length < 8):
                c_text = chipertext_bit[count * 64:count * 64 + 8 * chipertext_length]
                for i in range(0, 8 - chipertext_length):
                    c_text = c_text + '00000000'
            else:
                c_text = chipertext_bit[count * 64:count * 64 + 64]

            #ENKRIPSI DES
            encrypted_bin = self.enkripsi(iv, key_bit)

            iv = encrypted_bin
            plaintext_bit += self.xor(c_text, encrypted_bin)
            chipertext_length -= 8
            count += 1
        self.loop +=1
        return binascii.unhexlify('%x' % int(plaintext_bit, 2))
