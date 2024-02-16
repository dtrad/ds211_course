############################################
#              PART 1 FUNCTIONS            #
############################################

## Count the number of female and male citizens
# @param gender_list: a list of all citizen's genders
# @return the number of females and the number of males
def countGenders(gender_list):
    # Function stub
    num_females = 0
    num_males   = 0
    return num_females, num_males

## Find the average age of all citizens
# @param age_list: a list of all citizen's ages
# @return the average age of all citizens
def averageAge(age_list):
    # Function stub
    average_age = 0
    return average_age

## Find the age demographics of your citizens
# @param age_list: a list of all citizen's ages
# @return the number of children (ages 0-17)
# @return the number of adults   (ages 18-64)
# @return the number of seniors  (ages 65+)
def countAgeDemographics(age_list):
    # Function stub
    num_children = 0
    num_adults   = 0
    num_seniors  = 0

    return num_children, num_adults, num_seniors

## Return the number of citizens as well as the state of the census lists
# @param gender_list:    a list of all current citizen's genders
# @param age_list:       a list of all current citizen's ages
# @return the total number of citizens
# @return whether or not the gender_list and age_list have the same length
def citizenCount(gender_list, age_list):
    # Function stub
    num_citizens = 0
    valid_count = False
    return num_citizens, valid_count

## Make a new list of citizens' ages based on the given gender
# @param gender_list:    a list of all current citizen's genders
# @param age_list:       a list of all current citizen's ages
# @return a new list of ages for citizens of the given gender
def agesByGender(gender, gender_list, age_list):
    # Function stub
    new_age_list = []
    return new_age_list


############################################
#              PART 2 FUNCTIONS            #
############################################

## Add a citizen to our census
# @param new_gender:  the gender of the new citizen to be added
# @param new_age:     the age of the new citizen to be added
# @param gender_list: a list of all current citizen's genders
# @param age_list:    a list of all current citizen's ages
# @return updated gender list with citizen added
# @return updated age list with citizen added
def newCitizen(new_gender, new_age, gender_list, age_list):
    # Function stub
    return gender_list, age_list

## Remove a citizen from our census based on the index
# @param  ????? what should your parameters be ????
# @return ????? what should you return ????
def removeCitizen():
    # Function stub
    return 0

############################################
#                MAIN FUNCTION             #
############################################

def main():
    genders = ["male", "female", "female", "female", "male", "female"]
    # Define age list here
    
main()
