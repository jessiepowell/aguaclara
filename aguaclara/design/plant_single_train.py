from aguaclara.core.units import unit_registry as u
from aguaclara.design.floc import Flocculator
from aguaclara.design.sed_tank import SedimentationTank
from aguaclara.design.ent_tank import EntranceTank
from aguaclara.design.filter import Filter


class Plant:
    def __init__(self, q=20 * u.L/u.s,
                 temp=25 * u.degC,
                 ent_tank=EntranceTank(),
                 floc=Flocculator(),
                 sed=SedimentationTank(),
                 filter=Filter()):
        '''The 'inputs' for the plant recipe. Everything needed to make the plant is defined in this constructor. The
        UP classes are passed in to use as 'default values'. If we have to override the values, no problem, the
        user should understand that some variables get overridden depending on the 'plant design algorithm' used. For
        instance, the ent tank and flocculator lengths are sure to be overidden as they are interdependent.'''
        self.q = q
        self.temp = temp
        self.ent_tank = ent_tank
        self.floc = floc
        self.sed = sed
        self.filter = filter
        self.design_floc_and_ent_tank()
        self.design_sed_tank()

        # Now things can get 'moved around' as needed... vars can get passed around

    def design_floc_and_ent_tank(self):
        '''This is a 'design' function. It works through some design logic to change the instance in some way. This
        one happens to set the floc and ent_tank, so it is important to run during the constructor phase.'''
        #TODO: take the self.floc and self.ent_tank, and re-work until they are right, passing vars back and forth as necessary
        self.optimize_floc_and_ent_tank_area()
        pass

    def optimize_floc_and_ent_tank_area(self):
        '''Another 'design' function used to chunk the logic into more palatable blocks. Use descriptive function names
        often! They are better than comments in that they are easier to maintain and cleaner.'''
        pass

    def design_sed_tank(self):
        '''Same kindof function as design_floc_and_ent_tank - pass around params as needed based on the already designed
        floc and ent tank'''
        pass

    def design_filter(self):
        pass

    def get_total_volume(self):
        '''Example of a 'get' function... one that asks a question about the instance. The instance needs to do some
        work to get the answer to the query. Also known as a 'query' function.'''
        pass

    '''Don't yet think about how to pass the final properties to the CAD model. That'll be implemented in another step.
    I can help when we get there by using some YAML! You're right that we'll need a predictable way to transfer the
    instance data into the CAD model through some serialization step.'''