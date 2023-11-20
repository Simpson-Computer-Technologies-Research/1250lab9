import math

# Student class
class Student:
  points: int = 0
  year: int = -1
  is_coop: bool = False
  is_under_academic_probation: bool = False
  faces_academic_suspension: bool = False
  on_disciplinary_probation: bool = False
  has_vehicle: bool = False
  is_sas: bool = False
  walk_time: int = -1


  # Get the student answers
  def get_data(self) -> None:
    def is_yes(answer: str) -> bool:
      return 'y' in answer.lower()
    
    self.year = int(input("What year are you? (1-4) "))
    self.is_coop = is_yes(input("Are you in co-op? (y/n) "))
    self.is_under_academic_probation = is_yes(input("Are you under academic probation? (y/n) "))
    self.faces_academic_suspension = is_yes(input("Do you face academic suspension? (y/n) "))
    self.on_disciplinary_probation = is_yes(input("Have you been on Disciplinary Probation at any point during the Academic Year? (y/n) "))
    self.has_vehicle = is_yes(input("Do you have a vehicle? (y/n) "))
    self.is_sas = is_yes(input("Are you registered with SAS/Disability? (y/n) "))
    self.is_in_guelph = is_yes(input("Do you live in Guelph? (y/n) "))
    self.is_international = is_yes(input("Are you an international student? (y/n) "))
    self.walk_time = int(input("How long does it take to walk to your classes from choice 1 (in minutes)? "))


  # Calculate the students points depending on their inputted answers
  def calculate_points(self) -> None:
    # Determine points depending on whether the student is in co-op
    if self.is_coop:
      self.points += 1

    # Determine points depending on the student's year
    if self.year == 1:
      self.points += 4
    elif self.year == 2:
      self.points += 3
    elif self.year == 3:
      self.points += 2
    elif self.year == 4:
      self.points += 1

    # Determine points depending on whether the student is under academic probation
    if self.is_under_academic_probation:
      self.points -= 1

    # Determine points depending on whether the student has faced academic suspension
    if self.faces_academic_suspension:
      self.points -= 2

    # Determine points depending on whether the student has faced disciplinary probation
    if self.on_disciplinary_probation:
      self.points -= 3

    # Determine points depending on whether the student has a vehicle
    if not self.has_vehicle:
      self.points += 1

    # Determine points depending on whether the student is registered with SAS
    if self.is_sas:
      self.points += 1

    # Determine points depending on whether the student lives in Guelph
    if not self.is_in_guelph:
      if self.is_international:
        self.points += 10
      else:
        self.points += math.ceil(self.walk_time / 100)

    # Determine points depending on how long it takes to walk to class
    if self.walk_time < 10:
      self.points += 3
    elif self.walk_time > 10 and self.walk_time < 20:
      self.points += 2
    elif self.walk_time > 20:
      self.points += 1


# Main function
def main():
  # Create a new student object
  student = Student()

  # Get the student's data
  student.get_data()

  # Calculate the student's points
  student.calculate_points()

  # Print the student's points
  print("You have " + str(student.points) + " points")


# Run the main function
if __name__ == "__main__":
  main()
