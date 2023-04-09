class ChatID:
    def __init__(self , file = 'ChatIds.txt' ) -> None:
        self.PathFile = file
        with open(f'{file}' , 'r') as File :
            self.__ChatIDs__ = [int(item.strip('\n')) for item in File.readlines()]
        
    def Send(self , ChatID) -> bool:
        try :
            if ChatID not in self.__ChatIDs__ :
                with open(self.PathFile , 'a') as file :
                    file.write(f'{ChatID}\n')
                    self.__ChatIDs__.append(ChatID)
                    return True
        except : False
        
    def Get(self) -> list:
        with open(self.PathFile , 'r') as File :
            return [int(item.strip('\n')) for item in File.readlines()]


if __name__ == '__main__':
    test = ChatID('ChatIds.txt')
    print(test.__ChatIDs__)
    for i in range(20):
        test.Send(i)
    for i in range(20):
        test.Send(i)
    print(test.Get())