# Iniciação do Módulo de Sensor
class Sensor:

    # Método construtor da classe do Sensor
    def __init__(self, nome, tipo):
        self.__nome = nome
        self.__tipo = tipo

        # Por padrão o sensor terá valor desligado
        self.__estado_sensor = False

    
    def ligarSensor(self):

        # Caso o sensor esteja ligado
        if self.__estado_sensor:

            print("O sensor já está ligado!!! Por favor, não aperte novamente enquanto estiver ligado!")

        # Caso o sensor esteja desligado
        else:
               
            # Mude o estado do Sensor para ligado
            self.__estado_sensor = True
    

    def desligarSensor(self):

        # Caso o sensor esteja desligado
        if self.__estado_sensor:

            # Mude o estado do Sensor para ligado
            self.__estado_sensor = True

        # Caso o sensor esteja ligado
        else:
             
            print("O sensor já está desligado!!! Por favor, não aperte novamente enquanto estiver desligado!")


    # MÉTODOS GETERS E SETERS
    # Método get do nome do Sensor
    @property
    def nome(self):

        # Retonar o nome do Sensor
        return self.__nome

    # Método set do nome do Sensor
    @nome.setter
    def nome(self, nome_novo):

        self.__nome = nome_novo


    # Método get do estado do Sensor
    @property
    def estado_sensor(self):

        # Retonar o estado do Sensor
        return self.__estado_sensor
    

    # Método set do tipo Sensor
    @property
    def tipo(self):

        # Retonar o tipo do Sensor
        return self.__tipo


if __name__ == '__main__':
    sensor_1 = Sensor("Pessoal", "luz")
    sensor_1.ligarSensor()
    sensor_1.ligarSensor()
    print(sensor_1.estado_sensor)