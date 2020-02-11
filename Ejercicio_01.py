{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Practica 2"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Trabajando con clases    Ejercicio 1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "2020 Audi A4\n"
     ]
    }
   ],
   "source": [
    "class Car():\n",
    "    \"\"\"Clase tipo coche\"\"\"\n",
    "    def __init__(self, make, model, year):\n",
    "        \"\"\"Inicializacion de los atributos\"\"\"\n",
    "        self.make = make\n",
    "        self.model = model\n",
    "        self.year = year\n",
    "    \n",
    "    def get_descriptive_name(self):\n",
    "        \"\"\" Imprime las caracteristicas en la pantalla\"\"\"\n",
    "        long_name = str(self.year)+' '+self.make + ' ' + self.model\n",
    "        return long_name.title()\n",
    "\n",
    "my_new_car = Car('audi', 'a4',2020)\n",
    "print(my_new_car.get_descriptive_name())"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
