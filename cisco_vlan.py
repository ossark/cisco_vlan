class FilterModule(object):
    def filters(self):
        return {
            'cisco_vlan': self.cisco_vlan,
        }

    def cisco_vlan(self, data) :
        vlans = sorted(data, key=int)

        result = []
        start = end = vlans[0]

        try:
            for vlan in vlans :
                # Update end if we are in a "series"
                if vlan-1 == end : end = vlan

                # series is finished, output and seed start/end
                else :
                    result.append(str(start)) if start == end else result.append(str(start) +"-"+str(end))             
                    start = end = vlan

            # loop finished, output whatever is left in start/end
            result.append(str(start)) if start == end else result.append(str(start) +"-"+str(end)) 
        except Exception as e : return e

        del result[0]
        return result
