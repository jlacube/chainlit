import type { IMessageElement } from '@chainlit/react-client';

import { Element } from '@/components/Elements';

interface Props {
  elements: IMessageElement[];
}

const InlinedMCQList = ({ elements }: Props) => {
  if (!elements.length) {
    return null;
  }

  return (
    <div className="my-2 flex flex-col gap-3">
      {elements.map((element, index) => {
        return (
          <Element
            key={`${element.chainlitKey || element.id}-${index}`}
            element={element}
          />
        );
      })}
    </div>
  );
};

export { InlinedMCQList };
