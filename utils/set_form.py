from page_objects.spot_the_bugs import SpotTheBugs

# Always first set valid values
def set_form_valid_values(spot_the_bugs: SpotTheBugs):
    """
    This is to set valid values
    """
    spot_the_bugs.set_form_values(
        first_name="Sample First Name",
        last_name="Sample Last Name",
        phone="098877889900",
        country="India",
        email="dcsdfsf@cdsv.com",
        password="asdasfefhuweh" # This has to be moved to a file later
    )
    return spot_the_bugs