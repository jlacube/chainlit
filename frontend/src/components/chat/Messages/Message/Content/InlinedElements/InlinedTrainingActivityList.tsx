import type { ITrainingActivityElement } from '@chainlit/react-client';

import { Element } from '@/components/Elements';

interface Props {
  items: ITrainingActivityElement[];
}

const InlinedTrainingActivityList = ({ items }: Props) => {
  console.log('InlinedTrainingActivityList rendering items:', items);

  return (
    <>
      {items.map((element) => (
        <Element key={element.id} element={element} />
      ))}
    </>
  );
};

export { InlinedTrainingActivityList };
