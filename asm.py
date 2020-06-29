class Order(object):

    """base class: Order"""

    registers_dict = {
        '$zero': 0,
        '$at': 1,
        '$v0': 2,
        '$v1': 3,
        '$a0': 4,
        '$a1': 5,
        '$a2': 6,
        '$a3': 7,
        '$t0': 8,
        '$t1': 9,
        '$t2': 10,
        '$t3': 11,
        '$t4': 12,
        '$t5': 13,
        '$t6': 14,
        '$t7': 15,
        '$s0': 16,
        '$s1': 17,
        '$s2': 18,
        '$s3': 19,
        '$s4': 20,
        '$s5': 21,
        '$s6': 22,
        '$s7': 23,
        '$t8': 24,
        '$t9': 25,
        '$k0': 26,
        '$k1': 27,
        '$gp': 28,
        '$sp': 29,
        '$fp': 30,
        '$ra': 31,
    }
    orders = []

    def is_order(self, order_name):
        """judge the order in which class

        :order_name: TODO
        :returns: TODO

        """
        return order_name in self.orders


class R_Order(Order):

    """Type1: ROrder"""

    orders = [
        "add",
        "addu",
        "sub",
        "subu",
        "slt",
        "sltu",
        "and",
        "or",
        "xor",
        "nor",
        "sll",
        "srl",
        "sllv",
        "srlv",
        "srav",
        "mult",
        "multu",
        "div",
        "divu",
        "jalr",
        "eret",
        "syscall",
        "jr",
    ]

    def transfer(self, order_name: str, paras: str):
        """TODO: Docstring for transfer.

        :order_name: TODO
        :paras: TODO
        :returns: TODO

        """
        paralist = paras.split(' ')
        paralist_l = len(paralist)

        if paralist_l == 0:
            if order_name == 'eret':
                return (16 << 26) | ((16 & 31) << 21) | (24 & 63)
            elif order_name == 'syscall':
                return (0 << 26) | (12 & 63)
            else:
                return None
        elif paralist_l == 1:
            rs = paralist[0]
            if order_name == 'jr':
                value = self.registers_dict.get(rs)
                if value:
                    return (0 << 26) | (8 & 63) | (value << 21)
                else:
                    return None

            return None
        elif paralist_l == 2:
            rs = self.registers_dict.get(paralist[0])
            rt = self.registers_dict.get(paralist[1])
            if rs and rt:
                if order_name == 'mult':
                    return (0 << 26) | (24 & 63) | (rs << 21) | (rt << 16)
                elif order_name == 'multu':
                    return (0 << 26) | (25 & 63) | (rs << 21) | (rt << 16)
                elif order_name == 'div':
                    return (0 << 26) | (26 & 63) | (rs << 21) | (rt << 16)
                elif order_name == 'divu':
                    return (0 << 26) | (27 & 63) | (rs << 21) | (rt << 16)
                elif order_name == 'jalr':
                    return (0 << 26) | (9 & 63) | (rs << 21) | (rt << 11)
                else:
                    return None
            else:
                return None
        elif paralist_l == 3:
            rs = self.registers_dict.get(paralist[1])
            rt = self.registers_dict.get(paralist[2])
            rd = self.registers_dict.get(paralist[0])
            if rs and rd:
                if rt:
                    if order_name == 'add':
                        return ((0 << 26) | (32 & 63) | (rd << 11) | (rs << 21)
                                | (rt << 16))
                    if order_name == 'addu':
                        return ((0 << 26) | (33 & 63) | (rd << 11) | (rs << 21)
                                | (rt << 16))
                    if order_name == 'sub':
                        return ((0 << 26) | (34 & 63) | (rd << 11) | (rs << 21)
                                | (rt << 16))
                    if order_name == 'subu':
                        return ((0 << 26) | (35 & 63) | (rd << 11) | (rs << 21)
                                | (rt << 16))
                    if order_name == 'slt':
                        return ((0 << 26) | (42 & 63) | (rd << 11) | (rs << 21)
                                | (rt << 16))
                    if order_name == 'sltu':
                        return ((0 << 26) | (43 & 63) | (rd << 11) | (rs << 21)
                                | (rt << 16))
                    if order_name == 'and':
                        return ((0 << 26) | (36 & 63) | (rd << 11) | (rs << 21)
                                | (rt << 16))
                    if order_name == 'or':
                        return ((0 << 26) | (37 & 63) | (rd << 11) | (rs << 21)
                                | (rt << 16))
                    if order_name == 'xor':
                        return ((0 << 26) | (38 & 63) | (rd << 11) | (rs << 21)
                                | (rt << 16))
                    if order_name == 'nor':
                        return ((0 << 26) | (39 & 63) | (rd << 11) | (rs << 21)
                                | (rt << 16))
                    if order_name == 'sllv':
                        return ((0 << 26) | (4 & 63) | (rd << 11) | (rs << 21)
                                | (rt << 16))
                    if order_name == 'srlv':
                        return ((0 << 26) | (6 & 63) | (rd << 11) | (rs << 21)
                                | (rt << 16))
                    if order_name == 'srav':
                        return ((0 << 26) | (7 & 63) | (rd << 11) | (rs << 21)
                                | (rt << 16))
                elif paralist[2].isdigit():
                    if order_name == 'sll':
                        return ((0 << 26) | (rd << 11) | (rs << 21) |
                                (int(paralist[2]) & 31) << 6)
                    if order_name == 'srl':
                        return ((0 << 26) | (rd << 11) | (rs << 21) |
                                (int(paralist[2]) & 31) << 6 | (2 & 63))
                    if order_name == 'sra':
                        return ((0 << 26) | (rd << 11) | (rs << 21) |
                                (int(paralist[2]) & 31) << 6 | (3 & 63))
            return None


class I_Order(Order):

    """Type2: I_Order"""

    two_args_with_brackets = [
        "lw",
        "sw",
        "lh",
        "lhu",
        "sh",
    ]
    two_args = [
        "lui",
        "bgezal",
    ]
    three_args = [
        "addi",
        "addiu",
        "andi",
        "ori",
        "xori",
    ]
    three_args_with_label = [
        "beq",
        "bne",
    ]

    all_two_args = two_args.append(two_args_with_brackets)
    all_three_args = three_args.append(three_args_with_label)
    orders = all_two_args.append(all_three_args)

    def transfer(self, order_name: str, paras: str, PC: int, label_map: dict):
        """transfer I order into binary

        :order_name: TODO
        :paras: TODO
        :PC: TODO
        :label_map: TODO
        :returns: TODO

        """
        para_list = paras.split(' ')
        para_list_l = len(para_list)
        if order_name in self.two_args_with_brackets and para_list_l == 2:
            rt = self.registers_dict.get(para_list[0])
            tmp = para_list[1]
            start = tmp.find('(')
            end = tmp.find(')')
            if start == -1 or end == -1 or end <= start:
                return None
            rs = self.registers_dic.get(tmp[start+1, end])
            imm = tmp[0, start]
            if imm == "":
                imm = "0"
            if imm.isdigit() and rt and rs:
                if order_name == 'lw':
                    return ((35 << 26) | (rt << 16) | (int(imm) & 0xFFFF)
                            | (rs << 21))
                if order_name == 'sw':
                    return ((43 << 26) | (rt << 16) | (int(imm) & 0xFFFF)
                            | (rs << 21))
                if order_name == 'lh':
                    return ((33 << 26) | (rt << 16) | (int(imm) & 0xFFFF)
                            | (rs << 21))
                if order_name == 'lhu':
                    return ((37 << 26) | (rt << 16) | (int(imm) & 0xFFFF)
                            | (rs << 21))
                if order_name == 'sh':
                    return ((41 << 26) | (rt << 16) | (int(imm) & 0xFFFF)
                            | (rs << 21))
            else:
                return None
        if order_name in self.two_args and para_list_l == 2:
            rt = self.registers_dict.get(para_list[0])
            imm = self.registers_dict.get(para_list(1))
            if rt and imm.isdigit():
                if order_name == "lui":
                    return ((15 << 26) | (rt << 16) | imm & 0xFFFF)
                if order_name == "bgezal":
                    return ((1 << 26) | (17 & 31) << 16 | (rt << 21) |
                            ((int(imm) - PC) >> 2) & 0xFFFF)
                else:
                    return None
        if order_name in self.three_args_with_label and para_list_l == 3:
            rs = self.registers_dict.get(para_list[0])
            rt = self.registers_dict.get(para_list[1])
            label_address = label_map.get(para_list[2])
            if not label_address:
                if para_list[2].isdigit():
                    label_address = int(para_list[2])
                else:
                    return None
            if rs and rt:
                if order_name == 'beq':
                    return ((4 << 26) | (rs << 21) | (rt << 16) |
                            (((label_address - PC) >> 2) & 0xFFFF))
                if order_name == 'bne':
                    return ((5 << 26) | (rs << 21) | (rt << 16) |
                            (((label_address - PC) >> 2) & 0xFFFF))
                else:
                    return None
        if order_name in self.three_args and para_list_l == 3:
            rt = self.registers_dict.get(para_list[0])
            rs = self.registers_dict.get(para_list[1])
            imm = para_list[2]
            if rt and rs and imm.isdigit():
                if order_name == 'addi':
                    return ((8 << 26) | (rt << 16) | (rs << 21) |
                            (int(imm) << 21) & 0xFFFF)
                if order_name == 'addiu':
                    return ((9 << 26) | (rt << 16) | (rs << 21) |
                            (int(imm) << 21) & 0xFFFF)
                if order_name == 'andi':
                    return ((12 << 26) | (rt << 16) | (rs << 21) |
                            (int(imm) << 21) & 0xFFFF)
                if order_name == 'ori':
                    return ((13 << 26) | (rt << 16) | (rs << 21) |
                            (int(imm) << 21) & 0xFFFF)
                if order_name == 'xori':
                    return ((14 << 26) | (rt << 16) | (rs << 21) |
                            (int(imm) << 21) & 0xFFFF)
            else:
                return None


class Program(object):

    """mips Program"""

    def __init__(self, PC: int, label_map: dict):
        """init the program with PC

        :PC: TODO

        """
        self._PC = PC
        self._labelmap = label_map

    def exe(self, orders: str):
        """execute an order

        :order: TODO
        :returns: TODO

        """
        from re import split

        order_list = split('(\r\n|\r|\n)', orders)
        if not self.read_labels(order_list):
            return "Wrong label: Label must end with :"

        for order in order_list:
            self._PC += 4
            print('Start parsing : {}'.format(order))

            lst = order.split(' ')

            result = 0

            # if len(lst) != 1:
            # order_name = l[1]
            # if ROrder.isOrder(order_name):
            # result =

    def read_labels(self, order_list: list):
        """read labels form orders

        :order_list: TODO
        :returns: TODO

        """
        line_num = 0
        for order in order_list:
            label = order.split(' ')[0]
            if not label == '':
                if label[-1] == ':':
                    self._labelmap[label[0, -1]] = line_num
            else:
                return False
            line_num += 4
        return True


# print(R_Order().is_order('subt'))
